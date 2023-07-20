import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

def f(x):  # 定义函数
    return pow(x - 2.5, 2) + 3
def df(x):  # 函数的导数
    return 2 * x - 5

n = 0.01  # 学习率
e = 0.001  # 允许的最大误差
x=float(input('x的初始值：'))
mylist=[]
while 1:
    dy=df(x)
    if abs(dy)<e:
        break
    x=x-n*dy
    mylist.append(x)
print(f"极小值点x={x}, 极小值为f(x)={f(x)}")


m=np.array(mylist)
plt.scatter(m,f(m),color="r",marker='.')

y=np.arange(-8,10)
plt.plot(y,f(y))
plt.show()