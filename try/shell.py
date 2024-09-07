from pynput import mouse
import time
import threading
import keyboard


stop_flag = threading.Event()


def stop():
    while not stop_flag.is_set():
        try:
            if keyboard.is_pressed('ctrl+s'):
                print("Ctrl+s is pressed.")
                stop_flag.set()
                time.sleep(0.1)
                
        except AttributeError:
            pass
        print("Stop thread exiting...")


def on_mouse(x, y):  # 回调函数本身不应该有循环
    if not stop_flag.is_set():
        print(f"鼠标坐标是：({x},{y})")
        time.sleep(0.8)


def mouse_listener():
    with mouse.Listener(on_move=on_mouse) as listener:
        listener.join()
    print("Mouse listener exiting...")

    
if __name__ == "__main__":
    #  启动监听鼠标和键盘线程
    mouse_thread = threading.Thread(target=mouse_listener)
    keyboard_thread = threading.Thread(target=stop)

    mouse_thread.start()
    keyboard_thread.start()

    # 主线程进行计时

    try:
        while not stop_flag.is_set():
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("interrupted by users")
    finally:
        print("Setting stop flag...")
        stop_flag.set()  # 强行结束所有线程
        keyboard_thread.join()  # 循环终止就停止了？ 等待键盘检测完成
        mouse_thread.join()
        print("done!")
