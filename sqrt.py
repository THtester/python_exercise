# coding:UTF-8
import cmath


num = float(input("请输入一个数字："))
num_sqrt = num ** 0.5
print("%0.3.f的平方根为 %0.3%"%(num, num_sqrt))


# 计算实数和复数平方根
num = int(input("请输入一个数字："))
num_sqrt = cmath.sqrt(num)
print("{0}的平方根为{1:0.3f} + {2:0.3f}j".format(num, num_sqrt.real, num_sqrt.imag))