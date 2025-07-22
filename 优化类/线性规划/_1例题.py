# from scipy.optimize import linprog
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 设置中文显示
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# # 问题数据（转换为最小化问题）
# c = np.array([-30, -40])  # 目标函数系数（最大化转为最小化）
# A_ub = np.array([[2, 1],   # 不等式约束系数矩阵
#                  [1, 3]])
# b_ub = np.array([100, 120])  # 不等式约束右侧值
#
# bounds = [(0, None), (0, None)]  # 变量的上下界
#
# # 求解线性规划问题
# res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
#
# # 输出结果
# print(f"最优解: A产品 = {round(res.x[0], 2)} 单位, B产品 = {round(res.x[1], 2)} 单位")
# print(f"最大利润: {-res.fun:.2f} 元")
# print(f"人工使用: {2 * res.x[0] + res.x[1]:.2f} 小时")
# print(f"机器使用: {res.x[0] + 3 * res.x[1]:.2f} 小时")
# print(f"求解状态: {res.message}")
#
# # 可视化可行域和最优解
# x1 = np.linspace(0, 60, 100)
#
# # 约束1: 2x1 + x2 <= 100
# x2_1 = 100 - 2 * x1
#
# # 约束2: x1 + 3x2 <= 120
# x2_2 = (120 - x1) / 3
#
# # 绘制可行域
# plt.figure(figsize=(10, 6))
# plt.plot(x1, x2_1, 'r-', label='人工约束: $2x_1 + x_2 \\leq 100$')
# plt.plot(x1, x2_2, 'b-', label='机器约束: $x_1 + 3x_2 \\leq 120$')
# plt.fill_between(x1, np.minimum(x2_1, x2_2), 0, where=(x1 >= 0), color='gray', alpha=0.3)
#
# # 标记最优解点
# plt.plot(res.x[0], res.x[1], 'ro', markersize=8, label=f'最优解({res.x[0]:.1f}, {res.x[1]:.1f})')
#
# # 添加约束线和标注
# plt.axvline(0, color='k', linestyle='--', alpha=0.3)  # x1=0
# plt.axhline(0, color='k', linestyle='--', alpha=0.3)  # x2=0
#
# # 添加等利润线
# for profit in [800, 1200, 1600]:
#     x2_profit = (profit - 30 * x1) / 40
#     plt.plot(x1, x2_profit, 'g--', alpha=0.3)
#     plt.text(x1[-1]-5, x2_profit[-1]-5, f'Z={profit}', color='green', fontsize=9)
#
# # 设置图形属性
# plt.xlim(0, 60)
# plt.ylim(0, 100)
# plt.xlabel('A产品产量 ($x_1$)')
# plt.ylabel('B产品产量 ($x_2$)')
# plt.title('生产计划优化 - 可行域与最优解')
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend()
# plt.tight_layout()
# plt.savefig('linear_programming.png', dpi=300)
# plt.show()
#
