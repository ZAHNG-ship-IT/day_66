import numpy as np
from scipy.optimize import linprog
# 使用 A_ub 和 b_ub
# A_ub = np.array([[2, 1],   # 2x₁ + x₂ ≤ 100
#                  [1, 3]])  # x₁ + 3x₂ ≤ 120
# b_ub = np.array([100, 120])# 使用 A_eq 和 b_eq
#
#
# A_eq = np.array([[1, 1]])  # x₁ + x₂ = 50
# b_eq = np.array([50])
#
# # 原约束：x₁ + 2x₂ ≥ 30
# # 转换为：-x₁ - 2x₂ ≤ -30
# A_ub = np.array([[-1, -2]])  # 系数乘以-1
# b_ub = np.array([-30])       # 右侧值乘以-1from scipy.optimize import linprog

###################################################################################
###################################################################################
###################################################################################
###################################################################################
#综合实例
# 目标函数：最大化 Z = 3x₁ + 2x₂
# 转换为最小化：min(-Z) = -3x₁ - 2x₂
c = np.array([-3, -2])

# 约束条件：
# 1. x₁ + x₂ ≤ 40        (小于等于)
# 2. 2x₁ + x₂ ≥ 20       (大于等于，需转换)
# 3. x₁ - x₂ = 10        (等于)
# 4. x₁, x₂ ≥ 0          (非负约束)

# 小于等于约束
A_ub = np.array([[1, 1],      # x₁ + x₂ ≤ 40
                 [-2, -1]])   # -2x₁ - x₂ ≤ -20 (原：2x₁ + x₂ ≥ 20)
b_ub = np.array([40, -20])

# 等于约束
A_eq = np.array([[1, -1]])    # x₁ - x₂ = 10
b_eq = np.array([10])

# 变量边界（非负约束）
bounds = [(0, None), (0, None)]

# 求解
result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                bounds=bounds, method='highs')

print(f"最优解: x₁ = {result.x[0]:.2f}, x₂ = {result.x[1]:.2f}")
print(f"最优值: {-result.fun:.2f}")
print(f"求解状态: {result.message}")
#Optimization terminated successfully. 是 scipy.optimize.linprog 求解器返回的状态信息，表示优化过程成功完成。

# Status 0: Optimal - 找到最优解
# Status 1: Iteration limit reached - 达到迭代次数限制
# Status 2: Problem appears to be infeasible - 问题无可行解
# Status 3: Problem appears to be unbounded - 问题无界（目标函数可以无限优化）