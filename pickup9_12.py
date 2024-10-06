import pyautogui
import time  # 用于延时
import cv2  # 用于比对颜色，观察是否选中对应模块
import numpy as np
# import requests  
import sys
import argparse
import keyboard  # 用于检测键盘的行为
import threading
import os
from datetime import datetime
start_flag = False
interrupt_flag = True 
mouse_flag = True
start = 18
end = 22
screen_x = 0
screen_y = 0


def mouse_drag(start_x, start_y, end_x, end_y, duration=0.01):
    # 移动鼠标到起始位置
    pyautogui.moveTo(start_x, start_y)
    # 按下鼠标左键
    pyautogui.mouseDown()
    # 拖动到终点位置
    pyautogui.moveTo(end_x, end_y)
    # 释放鼠标左键
    pyautogui.mouseUp()


#  设置中断各线程
def listen_for_interrupt(start_hour, start_minute, start_second):
    global interrupt_flag
    global start_flag
    while True:
        if keyboard.is_pressed('ctrl+q'):
            interrupt_flag = False
            print("检测到Ctrl+Q，程序中断。")
            break
        now = datetime.now()
        if (now.hour == start_hour and now.minute == start_minute
            and now.second == start_second) or \
           (keyboard.is_pressed('ctrl+y')):
            start_flag = True
            

# 反馈鼠标位置，便于debug  或者新的界面坐标，便于更改相关参数
def mouse_track():  
    global mouse_flag
    while mouse_flag and interrupt_flag:
        x, y = pyautogui.position()
        posi = 'x:' + str(x).rjust(4) + ' y:' + str(y).rjust(4)
        print('\r', posi, end='')
        time.sleep(2)
        if keyboard.is_pressed('ctrl+m'):
            break


# 在气膜界面完成抢票/刷新的任务，其他抢票
def action():
    while True:
        global start_flag, interrupt_flag
        time.sleep(0.5)
        while interrupt_flag and start_flag:
            pyautogui.press('f5')
            #  1. 选择最新一天的场地位置
            time.sleep(3)
            pyautogui.click(600, 1000)  # 根据想要捡漏的日期进行调整，当天是600 最新一天是1900
            # 2. 滑轮下移
            mouse_drag(2540, 155, 2542, 486)  # 513为使用乒乓球界面进行测试，486为气膜界面
            time.sleep(0.1)
            # 放弃9-12，直接选1~4
            mouse_drag(1020, 1471, 1490, 1471)   # 再来一个鼠标横移，露出9~12部分的场地
           
            # 3. 根据时间选择截图位置
            if start is not None and end is not None:
                left = int(500)  # 考虑场地灯光，默认抢9~12号场，1100 场地坐标不需要动 妥协的话选400
                top = int((1105 + (start - 18) * 70))  # 截图范围的起始时间（不需要改）
                width = int(1520-left)  # 取的右边线，即12号场的位置
                height = int((end - start) * 70)  # 截图的高度由输入的时间决定
            else:
                left, top, width, height = 600, 737, 280, 200

            # 4. 截图并保存到文件夹
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

            # 创建/清空screenshot文件夹
            folder = 'pickup_qimo'
            if not os.path.exists(folder):
                os.makedirs(folder)
            else:
                for filename in os.listdir(folder):
                    file_path = os.path.join(folder, filename)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                    except Exception as e:
                        print(f"无法删除文件 {file_path}: {e}")

            screenshot_path = os.path.join(folder, 'latest_screenshot.png')
            cv2.imwrite(screenshot_path, screenshot)

            # 5. 检查截图区域是否有RGB为（255,191,42）的颜色// 通过颜色判定是否成功选上该场地
            target_color = np.array([42, 191, 255])  # OpenCV使用BGR顺序
            mask = cv2.inRange(screenshot, target_color, target_color)
            
            if np.any(mask):
                print("找到目标颜色")

                # 找到目标颜色的位置
                color_locations = np.where(mask)
                target_y, target_x = color_locations[0][0], \
                    color_locations[1][0]
                
                # 转换回全屏坐标
                screen_x = target_x + left
                screen_y = target_y + top
                
                # 点击目标颜色位置
                pyautogui.click(screen_x, screen_y)  # 点击有空的场次
                print("x= %d" % screen_x, "y = %d " % screen_y)
                time.sleep(0.05)
                # 执行额外的点击操作
                pyautogui.click(2000, 1450)  # 点击立即下单按钮
                time.sleep(0.05)
                pyautogui.click(984, 1130)  # 点击已知同意按钮
                time.sleep(0.05)
                pyautogui.click(1386, 1218)  # 点击立即支付
                time.sleep(0.5)
                print("程序执行完毕，退出。")
                interrupt_flag = False
                print("程序执行完毕，退出。")
                sys.exit(0)  # 退出整个程序
            else:
                print("未找到目标颜色，刷新页面并重复操作")
                mouse_drag(2540, 486, 2542, 155)  # 回位便于刷新
                # pyautogui.press('f5')  # 刷新页面
                time.sleep(0.01)  # 等待页面刷新
                now = datetime.now()
                if now.hour == 13 and now.minute == 0:
                    interrupt_flag = False
                    break
           
        if interrupt_flag is False:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("hour", type=int, help="抢票程序启动的时间")
    parser.add_argument("minute", type=int, help="抢票程序启动的时间")
    parser.add_argument("second", type=int, help="抢票程序启动的时间")
    parser.add_argument("-s", "--start", type=int, help="可接受的最早场次")
    parser.add_argument("-e", "--end", type=int, help="可接受的最晚场次")
    ans = parser.parse_args()
    start = ans.start
    end = ans.end
  

# 键盘监听/鼠标位置检测/自动抢票多线程启动
listener_thread = threading.Thread(target=listen_for_interrupt,
                                   args=(ans.hour,
                                         ans.minute,
                                         ans.second), daemon=True)
listener_thread.start()
mouse_thread = threading.Thread(target=mouse_track, daemon=True)
mouse_thread.start()
action_thread = threading.Thread(target=action, daemon=True)
action_thread.start()
# 阻塞主线程直到各线程结束
listener_thread.join()
mouse_thread.join()
action_thread.join()

'''
气膜蹲场使用指南：
 1、启动程序
    示例：在命令行中输入python <filename> -s 17 -e 22 12 0 1
    17 22 表示扫描17点~22点的场地 12 0 1 表示程序从12：00：01 开始运行
2、打开浏览器，全屏，登录、进入气膜界面，确保右侧滑块位于最顶端
3、按下“ctrl+y”，程序开始扫描，捡漏成功后自动停止，手动点击付款即可 需要全程停留在浏览器界面
4、按下“ctrl+Q”停止扫描，程序终止
 
'''

''' 
# 自动返回当前分辨率下鼠标坐标
try:
    while interrupt_flag:
        x, y = pyautogui.position()
        posi = 'x:' + str(x).rjust(4) + ' y:' + str(y).rjust(4)
        print('\r', posi, end='')
        time.sleep(2)

except KeyboardInterrupt:
    print('已退出！')
'''
