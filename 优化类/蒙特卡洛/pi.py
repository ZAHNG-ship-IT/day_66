import numpy as np
import matplotlib.pyplot as plt
## 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
def monte_carlo_pi(n_samples):
    # 在单位正方形内随机生成点
    x = np.random.uniform(-1, 1, n_samples)
    y = np.random.uniform(-1, 1, n_samples)

    # 计算点到原点的距离
    distances = np.sqrt(x**2 + y**2)

    # 统计落在单位圆内的点数
    inside_circle = np.sum(distances <= 1)

    # 估算π值：π = 4 * (圆内点数 / 总点数)
    pi_estimate = 4 * inside_circle / n_samples

    return pi_estimate, x, y, distances

# 不同样本量的收敛性分析
sample_sizes = [100, 1000, 10000, 100000,100000000]
pi_estimates = []

for n in sample_sizes:
    pi_est, _, _, _ = monte_carlo_pi(n)##这行代码的作用是调用 monte_carlo_pi(n) 函数，传入当前的样本数 n，并将返回的四个值中的第一个（π的估算值）赋给 pi_est，其余三个返回值（x、y、distances）用下划线 _ 忽略掉，不做后续处理。这样可以只关注 π 的估算结果。
    pi_estimates.append(pi_est)
    print(f"样本数: {n:6d}, π估值: {pi_est:.6f}, 误差: {abs(pi_est - np.pi):.6f}")

# 可视化
plt.figure(figsize=(12, 5))

# 子图1：点分布图
plt.subplot(1, 2, 1)
pi_est, x, y, distances = monte_carlo_pi(1000)
inside = distances <= 1
plt.scatter(x[inside], y[inside], c='red', s=1, alpha=0.6, label=f'圆内点 ({np.sum(inside)})')
plt.scatter(x[~inside], y[~inside], c='blue', s=1, alpha=0.6, label=f'圆外点 ({np.sum(~inside)})')

# 绘制单位圆
theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta), 'k-', linewidth=2)
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.gca().set_aspect('equal')
plt.title(f'蒙特卡洛估算π\n估值: {pi_est:.4f}')
plt.legend()
plt.grid(True, alpha=0.3)

# 子图2：收敛曲线
plt.subplot(1, 2, 2)
plt.semilogx(sample_sizes, pi_estimates, 'bo-', label='蒙特卡洛估值')
plt.axhline(y=np.pi, color='r', linestyle='--', label=f'真实值π = {np.pi:.6f}')
plt.xlabel('样本数量')
plt.ylabel('π估值')
plt.title('收敛性分析')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('monte_carlo_pi.jpg', dpi=300, bbox_inches='tight') # JPG格式
plt.show()

##蒙特卡洛方法是一种概率的思想