# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 15:52:07 2021

@author: HuYunlin

Python L1 
Action:
car_complain
"""

#数据加载
import pandas as pd

df = pd.read_csv('./car_complain.csv')
#print(df)
#df.to_excel('./car_complain.xlsx', index=False)
#导出为excel后缀应为.xlsx，False首字母需大写

df = df.drop('problem', axis=1).join(df.problem.str.get_dummies(','))
print(df)

