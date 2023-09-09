# 深入理解del操作
a = [1, -1, -10, 78, 16]
del a[1:2]
print(a)
del a[1]  # 删除当前被更新的列表a中的第二个元素
print(a)
del a[:]
print(a)
print()
b = set()
c1 = ('a', 'b', 'c')
c2 = list(c1)
# 注意:set中元素无法直接访问，只能通过for i in set中来遍历访问
d1 = {c1[i]: c2[len(c2)-i-1] for i in range(0, len(c1))}
for k, v in d1.items():
    print(k, v)
print(d1)
