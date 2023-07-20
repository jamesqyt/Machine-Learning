import numpy as np
import matplotlib.pyplot as plt

def f(x,y):   # 定义二元函数
    return x**2+y**2

def df(x):  # 求梯度函数
    return np.array([2*x[0],2*x[1]])

def gradient_descent(initial_x,learning_rate,nums):
    x = initial_x
    mylist=[]
    for i in range(nums):   # 迭代
        gradient=df(x)      # 计算梯度
        x=x-gradient*learning_rate      # 更新
        # 计算损失值
        loss = f(x[0],x[1])
        mylist.append(loss)
    return x,mylist

learning_rate = 0.01  # 学习率
nums = 100            # 迭代次数
np.random.seed(2)     # 设置随机数种子
initial_x = np.random.rand(2)*10    # 设置初始的x,y值
min_zhi, losses = gradient_descent(initial_x, learning_rate, nums)

print(f'最小值点是：{min_zhi}\n损失值：{losses}')


