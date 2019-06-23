#定义一个读取txt文件函数
def read_data():
    a=[]
    with open('E:\python\diesheg\data\date_1.txt') as f:
        d=f.readlines()
        for i in d :
            a.append(i.replace('\n','').split(','))
        return a

