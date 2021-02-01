# -*- coding: utf-8 -*-
"""
Action1：
计算2+4+……+100
"""

sum=0           #初始化求和为0
i=2             #初始化i，首项为2
while i<=100:   #循环语句，直到末项为100
    sum=sum+i
    i=i+2
print(sum)