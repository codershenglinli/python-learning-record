# 空数据类型的创建
empty_list = []
empty_set = set()
empty_tuple = ()
emoty_dict = {}
empty_dict2 = dict()

# 数据插入
# unfortunately, tuple is unchangeable /
# it doesn't have any inner function, except for len, max, min
empty_list.insert(0, 'firstvalue')
empty_set.update(empty_list)
empty_dict = {'Name': 'Runoob', 'Age': 19, 'First': 10}
# 数据修改
empty_list.index('firstvalue')
empty_list.append('secondvalue')
empty_set.__sizeof__(empty_list)

# 索引
a = 0
if a in empty_list:
    print('0在列表中，列表可以索引')
else:
    print('0不在列表中')

# 查找


# 清空
empty_list.clear
empty_set.clear

# 输出
print(empty_tuple)
print(empty_list)
print(empty_set)
print(empty_dict)

# del
del empty_tuple
del empty_list
del empty_set
del empty_dict
print('\n')
print('这是新的一行')
