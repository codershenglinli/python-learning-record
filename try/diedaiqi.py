class MyNumbers:
    def __iter__(self):
        self.a = 1
        print(type(self))
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
# print('myclass的类型为',  type(myclass))
myiter = iter(myclass)

'''    # 输出形式一
    ans = set(myiter)
    print(ans)  # 这一步会自动输出两个值
'''

'''# 输出形式二
while True:
    try:
        print(next(myiter))
    except StopIteration:
        None

'''   # 输出形式三
for i in myiter:
    print(i)
