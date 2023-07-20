import numpy as np

def zhi(arr):
    return np.linalg.matrix_rank(arr)

#化为行阶梯型矩阵
def aa(arr):
    row_len,l_len=arr.shape # 行数、列数
    arr = arr.astype(float)
    for i in range(l_len-1):
        # 求列上最大值的索引
        l = np.argmax(arr[i:, i]) + i
        # 交换第i行
        arr[[i,l]] = arr[[l,i]]
        if arr[i,i] != 0:
            # 该列的首非零元化为一
            arr[i] = arr[i] / arr[i,i]
            # 列上的化为0
            for j in range(i+1,row_len):
                arr[j] = arr[j] - arr[j,i] * arr[i]
    return arr


# 回代求解
def huidai(arr):
    if (zhi(arr[:,:-1]) != zhi(arr)):
        print('方程组无解')
    row_len = arr.shape[0]
    x=np.zeros(row_len)
    for n in range(row_len-1,-1,-1):
        x[n] = arr[n,-1]
        for m in range(n+1,row_len):
            x[n] -= arr[n,m]*x[m]
    return x

def zz(arr):
    print("原数组是：\n",arr)
    print('数组化为行阶梯型：\n',aa(arr))
    print('得到的值是：\n',huidai(aa(arr)))


if __name__ == '__main__':
    a = np.array([[1, 1, 0, 0, 3],
                  [0, 0, 1, 1, 8],
                  [1, 0, 1, 0, 4],
                  [0, 1, 0, 1, 7]])
    zz(a)