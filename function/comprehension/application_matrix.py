# 利用推导式进行矩阵的转置/求行列式的值等操作
# 矩阵的转置
def matrix():
    if __name__ == '__main__':
        matrix1 = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
        print([[row[i] for row in matrix1] for i in range(0, len(matrix1[1]))])
    else:
        print('被另一模块引入了')