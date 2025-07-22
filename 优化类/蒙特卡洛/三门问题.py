# import numpy as np
# import matplotlib.pyplot as plt
#
# # 设置中文字体
# plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
# plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['font.size'] = 10


import numpy as np
import matplotlib.pyplot as plt

# 优化字体配置，消除警告
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimSun', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 10

# 设置负号和特殊字符的处理
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False



def monty_hall_simulation(n_simulations, strategy='switch'):
    """
    三门问题蒙特卡洛模拟

    参数:
    n_simulations: 模拟次数
    strategy: 策略 'switch'(换门) 或 'stay'(不换门)

    返回:
    获胜次数, 获胜率
    """
    wins = 0

    for _ in range(n_simulations):
        # 1. 随机将奖品放在三门中的一门后面 (0, 1, 2)
        prize_door = np.random.randint(0, 3)

        # 2. 参赛者随机选择一门
        player_choice = np.random.randint(0, 3)

        # 3. 主持人开启一扇没有奖品且参赛者未选择的门
        # 找出主持人可以开启的门
        available_doors = [door for door in range(3)
                          if door != player_choice and door != prize_door]

        # 如果参赛者选中了奖品门，主持人可以开启剩余两门中的任意一门
        if player_choice == prize_door:
            host_opens = np.random.choice([door for door in range(3)
                                         if door != player_choice])
        else:
            # 如果参赛者没选中奖品门，主持人只能开启那扇既不是奖品门也不是参赛者选择的门
            host_opens = available_doors[0]

        # 4. 根据策略决定最终选择
        if strategy == 'switch':
            # 换门：选择剩下的那扇门
            final_choice = [door for door in range(3)
                           if door != player_choice and door != host_opens][0]
        else:
            # 不换门：坚持原来的选择
            final_choice = player_choice

        # 5. 检查是否获胜
        if final_choice == prize_door:
            wins += 1

    win_rate = wins / n_simulations
    return wins, win_rate

def comprehensive_monty_hall_analysis():
    """三门问题综合分析"""

    # 不同的模拟次数
    simulation_sizes = [100, 1000, 5000, 10000, 50000, 100000]

    switch_rates = []
    stay_rates = []

    print("三门问题蒙特卡洛模拟结果:")
    print("=" * 60)
    print(f"{'模拟次数':<10} {'换门策略胜率':<15} {'不换门策略胜率':<15} {'差值':<10}")
    print("-" * 60)

    for n in simulation_sizes:
        # 换门策略
        switch_wins, switch_rate = monty_hall_simulation(n, 'switch')

        # 不换门策略
        stay_wins, stay_rate = monty_hall_simulation(n, 'stay')

        switch_rates.append(switch_rate)
        stay_rates.append(stay_rate)

        print(f"{n:<10} {switch_rate:<15.4f} {stay_rate:<15.4f} {switch_rate-stay_rate:<10.4f}")

    # 理论值
    theoretical_switch = 2/3
    theoretical_stay = 1/3

    print("-" * 60)
    print(f"{'理论值':<10} {theoretical_switch:<15.4f} {theoretical_stay:<15.4f} {theoretical_switch-theoretical_stay:<10.4f}")

    # 可视化结果
    plt.figure(figsize=(15, 10))

    # 子图1: 胜率收敛图
    plt.subplot(2, 2, 1)
    plt.semilogx(simulation_sizes, switch_rates, 'bo-', label='换门策略', linewidth=2, markersize=8)
    plt.semilogx(simulation_sizes, stay_rates, 'ro-', label='不换门策略', linewidth=2, markersize=8)
    plt.axhline(y=theoretical_switch, color='blue', linestyle='--', alpha=0.7, label='理论值(换门): 2/3')
    plt.axhline(y=theoretical_stay, color='red', linestyle='--', alpha=0.7, label='理论值(不换门): 1/3')
    plt.xlabel('模拟次数')
    plt.ylabel('获胜率')
    plt.title('三门问题：策略胜率收敛分析')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 1)

    # 子图2: 误差分析
    plt.subplot(2, 2, 2)
    switch_errors = [abs(rate - theoretical_switch) for rate in switch_rates]
    stay_errors = [abs(rate - theoretical_stay) for rate in stay_rates]

    plt.loglog(simulation_sizes, switch_errors, 'bo-', label='换门策略误差')
    plt.loglog(simulation_sizes, stay_errors, 'ro-', label='不换门策略误差')
    plt.xlabel('模拟次数')
    plt.ylabel('绝对误差')
    plt.title('误差收敛分析')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # 子图3: 单次详细模拟可视化
    plt.subplot(2, 2, 3)
    n_detailed = 1000
    switch_wins, switch_rate = monty_hall_simulation(n_detailed, 'switch')
    stay_wins, stay_rate = monty_hall_simulation(n_detailed, 'stay')

    strategies = ['换门策略', '不换门策略']
    win_rates = [switch_rate, stay_rate]
    colors = ['skyblue', 'lightcoral']

    bars = plt.bar(strategies, win_rates, color=colors, alpha=0.8, edgecolor='black')
    plt.axhline(y=theoretical_switch, color='blue', linestyle='--', alpha=0.7)
    plt.axhline(y=theoretical_stay, color='red', linestyle='--', alpha=0.7)

    # 在柱状图上显示数值
    for bar, rate in zip(bars, win_rates):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{rate:.3f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.ylabel('获胜率')
    plt.title(f'策略对比 (n={n_detailed})')
    plt.ylim(0, 1)
    plt.grid(True, alpha=0.3, axis='y')

    # 子图4: 问题说明图
    plt.subplot(2, 2, 4)
    plt.text(0.05, 0.9, '三门问题说明:', fontsize=14, fontweight='bold', transform=plt.gca().transAxes)

    explanation = """
1. 游戏开始时有三扇门，其中一扇门后有奖品
2. 参赛者选择一扇门（不打开）
3. 主持人打开剩余两扇门中没有奖品的一扇
4. 参赛者可以选择：
   - 坚持原来的选择（不换门）
   - 改选剩下的那扇门（换门）

数学分析：
• 初始选择正确的概率：1/3
• 初始选择错误的概率：2/3
• 换门策略胜率：2/3
• 不换门策略胜率：1/3

结论：换门策略的获胜概率是不换门的2倍！
    """

    plt.text(0.05, 0.05, explanation, fontsize=10, transform=plt.gca().transAxes,
            verticalalignment='bottom', bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.8))
    plt.axis('off')

    plt.tight_layout()

    # 保存图像
    plt.savefig('三门问题蒙特卡洛分析.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

    return switch_rates, stay_rates

# 运行详细分析
if __name__ == "__main__":
    switch_rates, stay_rates = comprehensive_monty_hall_analysis()

    print("\n" + "="*60)
    print("结论验证:")
    print(f"大样本下换门策略胜率: {switch_rates[-1]:.4f} ≈ {2/3:.4f}")
    print(f"大样本下不换门策略胜率: {stay_rates[-1]:.4f} ≈ {1/3:.4f}")
    print(f"换门策略优势: {switch_rates[-1] - stay_rates[-1]:.4f}")