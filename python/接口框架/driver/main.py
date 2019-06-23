#driver 中主要是控制跑回归测试时只跑那些模块的用列
from 接口框架.report.baogao import baogao
with open ('a.txt','r') as f:
    a=f.readlines()
    if 'all' in a:
        baogao('*')
    else:
        baogao(a)
