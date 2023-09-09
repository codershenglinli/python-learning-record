from function.comprehension import application_matrix
application_matrix.matrix()
'''
test.function()
print('测试列表推导式')
name = ['bond', 'john', 'anthony', 'bt', 'gaisi']
names = [it.upper() for it in name if len(it) > 4]
print(names)
print('使用字符串长度推导字典')
str1 = {'I have to learn python', 'woce'}
dict1 = {key: len(key) for key in str1}
print(dict1)

print('练习使用集合推导式')
print('利用集合推导式，提取一个字符串中的单词')
str2 = 'baby my lover, please don\'t hurt me'
list1 = [i for i in range(len(str2)) if str2[i] == ' ']
set2 = (str2[list1[i] + 1:list1[i+1]] for i in range(len(list1) - 1))
print(list1)
tuple2 = tuple(set2)
print(tuple2)
'''
