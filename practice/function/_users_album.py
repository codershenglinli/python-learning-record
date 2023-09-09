def make_album(result, singer, album):
    result[singer] = album
    return result


out = dict()
while True:
    print("输入你喜欢的歌手的名字：")
    singer = input()
    print("她/他最受欢迎的作品是？")
    album = input()
    if singer == '%' or album == '%':
        break 
    out = make_album(out, singer, album)
    # 退出条件
    print("(please enter '%' at any time to quit)")
   

print(out)
