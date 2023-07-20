import numpy as np
import matplotlib.pyplot as plt

# 定义二元函数
def f(x, y):
    return x**2 + y**2  # 二元函数: f(x, y) = x^2 + y^2

# 创建平面上的网格点
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 计算二元函数在每个网格点上的值
Z = f(X, Y)

# 绘制二元函数的图像
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')

ax.set_ylabel('Y')

ax.set_zlabel('f(X, Y)')

ax.set_title('Plot of the 2D Function')
plt.show()
