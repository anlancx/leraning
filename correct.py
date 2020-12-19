"""
计算值校正
"""

calculate_value = float(input('请输入计算结果(nm):'))
correct_value = float(input("请输入Sr(R)的值(a.u.)："))

if correct_value <= 0.68467:
    a = 0.68467
else:
    a = correct_value

emission_value = round(calculate_value * (0.89809 / a))
print(f'最大发射峰位置：{emission_value}nm')
