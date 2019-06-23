# -*- coding: utf-8 -*- 

# @Time : 2019/6/11 上午11:09 

# @Author : 废柴 

# @Project: douyun

# @FileName : config_1.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================


# 定义一个读取txt文件的函数
def read_data():
    datas = []
    with open(r'E:\python\DieSheng\data\data_1.txt', 'r') as fb:
        d = fb.readlines()
        for i in d:
            datas.append(i.replace('\n', '').split(','))
    return datas
