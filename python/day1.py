# !/usr/bin/python
# _*_ coding:utf-8 _*_
# import copy
# # c=[1,5,2,7,3,6,4]
# # a=[1,5,c,8,9]
# # ff =copy.deepcopy(a)
# # c.append(13)
# # print(a)
# # print(ff)
# # a=[12,13,15,16,15]
# # a[0]=11
# # print(a)
# # a={"name":"小明","age":20}
# # b={"sex":"nan"}
# # a.update(b)
# # print(a)
# # a={12,13,15,"wq"}
# # b={16,19,13}
# # print(a-b)
# # a="user{}"
# #  print("%s*%s=%s"%(1,2,1*2))
# # a=[1,2,3]
# # b=[2,6,7]
# # print("{}*{}".format(a,b))
# # 判断成绩处于什么层次
# # a=input("请输入一个成绩")
# # a=int(a)
# # if a >= 90 and a <= 100:
# #     print("优秀")
# # elif a<90 and a >=80:
# #     print("良好")
# # elif a<80 and a>=70:
# #     print("及格")
# # else:
# #     print("不及格")
# # a=input("手动输入一个数字")
# # a=int(a)
# # if a%2==0:
# #     if a%3==0:
# #       print("helloworld")
# #     else:
# #       print("hello")
# # elif a%3==0:
# #  print("world")
# # else:
# #  print(123)
# # a=0
# # b=0
# # for i in range(1,100,2):
# #  a=a+i
# # for j in range(2,100,2):
# #   b=b-j
# # print(a+b)
# # b=0
# # a=0
# # for i in range(1,100):
# #     if i%2==0:
# #         a=a+i
# # else:
# #     print(b-a)
# # for i in range(1,10):
# #     for j in range(1,10):
# #      print("{}*{}".format(i,j))
# #  import randomn
# #  a=random.randrange(1,10)
# #  for i in range(3):
# #    b=input("请输入一个数")
# #    b=int(b)
# #    if b==a:
# #         print("恭喜")
# #    elif b>a:
# #         print("大一点")
# #    else:
# #      print("小一点")
# # 9.	三次猜数字
# # import random
# # a=random.randrange(1,10)
# # for i in range(1,4):
# #     b=input("请输入一个数")
# #     b=int(b)
# #     if b==a:
# #         print("恭喜")
# #         break
# #     elif b>a:
# #         print("大一点还有{}次机会".format(3-i))
# #     else:
# #         print("小一点还有{}次机会".format(3-i))
# # else:
# #     print("菜")
# # 乘法口诀表;
# # for i in range(1,10):
# #     for j in range(1,i+1):
# #        print("{}*{}={}".format(i,j,i*j),end="\t")
# #     print()
# #质数之和
# # b=0
# # for i in range(2,101):
# #     for j in range(2,i+1):
# #         a=i%j
# #         if a==0:
# #             break
# #     if i==j:
# #         b=b+i
# # print(b)
# #因数
# # for i in range(2,1001):
# #     num=0
# #     for j in range(1,i):
# #         a=i%j
# #         if a==0:
# #             num=num+j
# #     if num==i:
# #         print(i)
# #水仙花数
# # for i in range(1,10):
# #     for j in range(0,10):
# #         for q in range(0,10):
# #             a=i*100+j*10+q
# #             b=i**3+j**3+q**3
# #             if a==b:
# #                 print(a)
# # 阶乘之和
# # c=input("请输入一个数")
# # c=int(c)
# # a=1
# # b=0
# # for i in range(1,c+1):
# #     a=i*a
# #     b=b+a
# # print(b)
# # 回文字符串
# # a=input("请输入一个字符串")
# # b=len(a)
# # c=b//2
# # for i in range(0,c):
# #     if a[i]==a[-1-i]:
# #         if i==c-1:
# #          print("是一个回环数字串")
# #     else:
# #         print("不是一个回环数字")
# # i=1
# # a=0
# # while i < 101:
# #     a=i+a
# #     i=i+1
# # print(a)
# #求平均数，小于平均数的数
# # while True:
# #   a=input(">>")
# #   a=a.split(",")
# #   a=[int(i) for i in a]
# #   b=sum(a)//len(a)
# #   if a[0]<0:
# #       break
# #   print(b)
# #   c=[k for k in a if k<b]
# #   print(c)
# # 去重
# # a=input(">>")
# # a=a.split(",")
# # a=[int(i) for i in a]
# # for j in a:
# #     b=a.count(j)
# #     if b>1:
# #         for q in range(b-1):
# #             a.remove(j)
# # print(a)
# # 去重
# # a=[12,12,12,13,14]
# # b=[]
# # for i in a:
# #     if i not in b:
# #         b.append(i)
# # print(b)
# # 打印乘法口诀表
# # f = open(r"a..txt","w",encoding="utf-8")
# # for i in range(1,10):
# #     for j in range(1,i+1):
# #       f.write("{}*{}={}\t".format(i,j,i*j))
# #     f.write("\n")
# # f.close()
# # 过滤以abc开头的行
# # f = open(r"a.txt","r",encoding="utf-8")
# # a=f.readlines()
# # for i in a:
# #     if i[:3]=="abc":
# #         print(i)
# # f = open(r"a.txt","r",encoding="utf-8")
# # 查看文件15-20内容
# # for i in range(1,21):
# #     if i<15:
# #       f.readline()
# #     else:
# #         print(f.readline())
# # 选择
# # a=input("请输入一组数")
# # a=a.split(" ")
# # a=[int(i) for i in a]
# # b=len(a)
# # for j in range(0,b):
# #     for k in range(j+1,b):
# #         if a[j]>a[k]:
# #             t=a[j]
# #             a[j]=a[k]
# #             a[k]=t
# # print(a)
# # 冒泡
# # a=input("请输入一组数")
# # a=a.split(" ")
# # a=[int(i) for i in a]
# # b=len(a)
# # for j in range(1,b):
# #     for k in range(0,b-1):
# #         if a[k]>a[k+1]:
# #             t=a[k]
# #             a[k]=a[k+1]
# #             a[k+1]=t
# # print(a)
#
# # a=input("请输入三条边")
# # a=a.split(" ")
# # a=[int(i) for i in a]
# # if a[0]+a[1]>a[2]:
# #     if a[0]-a[1]<a[2]:
# #        print("是一个三角形")
# #     else:
# #        print("不是一个三角形")
# # else:
# #     print("不是一个三角形")
# # # 打印列表所有第一大跟第二大的数
# # a=input("请输入一组数")
# # a=a.split(" ")
# # a=[int(i) for i in a]
# # a.sort()
# # b=a.count(a[-1])
# # c=[]
# # for j in range(b):
# #     c.append(a[-1])
# #     a.remove(a[-1])
# # d=a.count(a[-1])
# # for j in range(d):
# #     c.append(a[-1])
# # print(c)
# # 不用int把字符串变为整数
# # a="123"
# # b=a[::-1]
# # c=0
# # for i in range(len(a)):
# #     for j in range(0,10):
# #         if b[i]==str(j):
# #             c=c+j*10**i
# # print(c)
# # 一组数往左移
# # a=input("请输入一组数")
# # a=a.split(" ")
# # a=[int(i) for i in a]
# # b=len(a)
# # t=a[0]
# # for i in range(len(a)-1):
# #     a[i]=a[i+1]
# # a[-1]=t
# # print(a)
# # 追加a 写入
# # 下载图片
# # f = open("abc.jpg",'rb')
# # b=f.read()
# # f.close()
# # ff=open("a1.jpg","wb")
# # ff.write(b)
# # ff.close()
# # with open("a.txt","r+",encoding="utf-8")as f:
# #     b=f.read()
# #     f.write("123")
# # print(b)
# # def a():
# #     b=0
# #     for i in range(1,101):
# #         b=b+i
# #     print(b)
# # a()
# # 19.	用100元买100只鸡，公鸡2元一只，母鸡1元一只，小鸡0.5元一只，问买公鸡、母鸡、小鸡各几只
# # for x in range(1,101):
# #     for y in range(1,101):
# #         for z in range(1,101):
# #             if x+y+z==100:
# #                 if 2*x+y+0.5*z==100:
# #                     print(x,y,z)
# # 13.	任意4个数字，组成不相同的三位数
# # a=input("任意输入四个数")
# # a=a.split(" ")
# # a=[int(i) for i in a]
# # for j in a:
# #     for k in a:
# #         if j != k:
# #             for q in a:
# #                 if q!=k and q!=j:
# #                     b=j*100+k*10+q
# #                     print(b)
# # 5.	判断以什么开头，以什么结束
# # a=input("请输入一串字符串")
# # b=a.startswith("qw")
# # c=a.endswith("rt")
# # if b==True:
# #       if c==True:
# #             print(a)
# #       else:
# #             print("false")
# # else:
# #       print("false")
# # # 17.	将列表中最大的放在最后一位，最小的放在第一位
# # 错脚本
# # a=input(">>")
# # a=a.split(" ")
# # a=[int(i) for i in a]
# # c=[j for j in a]
# # c.sort()
# # print(c)
# # a=input(">>")
# # a=a.split(" ")
# # a=[int(i) for i in a]
# #
# # for i in range(len(a)):
# #       if a[i]==c[0]:
# #             a.remove(a[i])
# #             a[0]=a[i]
# #       elif a[i]==c[-1]:
# #             a.remove(a[i])
# #             a[-1]=a[i]
# # print(a)
# # 17.	将列表中最大的放在最后一位，最小的放在第一位
# # a=input(">>")
# # a=a.split(" ")
# # a=[int(i) for i in a]
# # c=[j for j in a]
# # c.sort()
# # a.remove(c[0])
# # a.remove(c[-1])
# # a.insert(0,c[0])
# # a.append(c[-1])
# # print(a)
#
# # 更改全局变量
# # b=0
# # def a():
# #      global b
# #      b=1
# #      print(b)
# # a()
# # print(b)
# # 传参
# # def a(x):
# #       print("qqq")
# #       print(x)
# # a(164578)
# # def a(x):
# #       a=sum(range(x+1))
# #       print(a)
# # a(100)
# # def a(x,y):
# #       a=sum(range(x,y+1))
# #       print(a)
# # a(0,100)
# # 默认参数
# # def a(b=100):
# #       a=sum(range(b+1))
# #       print(a)
# # a(10)
# # def a(x,y):
# #       b=0
# #       for i in range(x,y+1):
# #             num=0
# #             for j in range(1,i+1):
# #                   a=i%j
# #                   if a==0:
# #                    num=num+1
# #             if num==2:
# #                   b=b+i
# #       print(b)
# # a(1,9)
# # 可变长参数(将这些数据放入到一个元组中）
# # def a(*x):
# #       print(x)
# # a(1,15,16,18)
# # 传入的数据必须是键值对(相当于字典)
# # def a(**x):
# #       print(x)
# # a(name=123,age=678)
# # # 赋值将a的值赋予c(b）
# # def c(b):
# #       a=0
# #       for i in range(1,b+1):
# #             a=a+i
# #       print(a)
# #       return a
# # print(c(100)+2)
# # 加2(1=10,1-20,1-30,1-40)
# # def c(b):
# #       a=0
# #       for i in range(1,b+1):
# #             a=a+i
# #       print(a)
# #       return a
# # for i in range(10,40,10):
# #       b=c(i)+2
# #       print(b)
#
# #
# # def a(x,y,z):
# #       if y=="+":
# #             b=x+z
# #       elif y=="-":
# #             b=x-z
# #       elif y=="*":
# #             b=x*z
# #       elif y=="/":
# #             b=x/z
# #       return b
# # print(a(2,"-",2))
#
# # a=lambda x,y : x+y
# # b=lambda x,y : x-y
# # c=lambda x,y : x*y
# # d=lambda x,y : x/y
# # s=input(">>")
# # if "+" in s:
# #       e=s.split("+")
# #       print(a(int(e[0]),(e[1])))
# # elif "-" in s:
# #       f=s.split("-")
# #       print(b(int(f[0]),(f[1])))
# # elif "*" in s:
# #       g=s.split("*")
# #       print(c(int(g[0]),(g[1])))
# # elif "/" in s:
# #       h=s.split("/")
# #       print(d(int(h[0]),(h[1])))
#
# # def a(x,y,z):
# #       x=list(x)
# #       b=y+z
# #       if b > len(x):
# #           b=len(x)
# #       for i in range(y,b):
# #             x.pop(y)
# #       x="".join(x)
# #       print(x)
# # a("qwer",1,2)
# #删除下标为1后的五个数（包括下表为1的数）
# # def a(x,y,z):
# #       x=list(x)
# #       b=y+z
# #       if b>len(x):
# #          b=len(x)
# #       for i in range(y,b):
# #             x.pop(y)
# #       x=str(x)
# #       print(x)
# # a("qwer",1,5)
#
# # 20.	一个函数，传两个参数a,b，a是数组，b是一个数字，找出a数组中两数只和等于b，打印出来这两个数
# # def a(a,b):
# #       for j in range(len(a)):
# #             for k in range(len(a)):
# #                   if a[j]+a[k]==b:
# #                         print(a[j],a[k])
# # a([1,2,3,4,5],3)
# # 21.	统计.Cpp文件有多少行，统计的时候将文件中的空行、单行注释的行去除
# # with open("a.txt","r",encoding="utf-8") as f:
# #       b=f.readlines()
# #       print(len(b))
# #       for i in range(len(b)-1):
# #             if b[i]=="\n":
# #                   b.pop(i)
# #       for i in range(len(b)-1):
# #             c=b[i].startswith("#")
# #             if c==True:
# #                 b.pop(i)
# # print(b)
#
# # 18.	一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# # a=input("请输入一组数")
# # a=a.split(" ")
# # b=input("请输入一个数")
# # a.append(b)
# # a=[int(j) for j in a]
# # for i in range(1,len(a)):
# #     for k in range(0,len(a)-1):
# #         if a[k]>a[k+1]:
# #             t=a[k]
# #             a[k]=a[k+1]
# #             a[k+1]=t
# # print(a)
# # 15.	进制转换
# # def a(x,y):
# #     if y==16:
# #         print(hex(x))
# #     elif y==2:
# #         print(bin(x))
# #     elif y==8:
# #         print(oct(x))
# # a(10,8)
# # 10进制转16进制
# # a=int(input(">>"))
# # ff=[str(i) for i in range(10)]+["a","b","c","d","e","f"]
# # print(ff)
# # c= ""
# # while True:
# #     b=a%16
# #     c=c+ff[b]
# #     a=a//16
# #     if a==0:
# #         break
# # print(c[::-1])
# # 判断三角形
# # a=input("请出入三条边")
# # a=a.split(" ")
# # a=[int(i) for i in a]
# # a.sort()
# # if a[0]+a[1]>a[2]:
# #     if a[0]**2+a[1]**2==a[2]**2:
# #         print("是直角三角型")
# #         if a[0]==a[1]:
# #             print("是一个等腰三角形")
# #     elif a[0] ** 2 + a[1] ** 2>a[2] ** 2:
# #         print("是一个锐角三角形")
# #         if a[0] == a[1] and a[0] == a[1]:
# #             print("是一个等边三角")
# #         if a[0]==a[1]:
# #             print("是一个等腰三角形")
# #     elif a[0] ** 2 + a[1] ** 2 < a[2] ** 2:
# #         print("是一个钝角三角型")
# #         if a[0]==a[1]:
# #             print("是一个等腰三角形")
# # else:
# #     print("不是三角形")
# # def a():
# #     print("123")
# # def b():
# #     print("46")
# # if __name__ == "__main__":
# #     print(7897)
# # 异常处理：
# # 异常：代码由于逻辑结构或者语法错误导致的程序中断
# # 异常处理：对将要发生的异常进行预防和处理
# # try:
# #     a=123+"qew"
# #     print(a)
# # except:#默认能够预防所有类型的错误
# #     print(678)
# # try:
# #     a=123+"wq"
# #     print(a)
# # except Exception as e:
# #     print(e)
# # try:
# #     a=1+2
# #     print(a)
# # except:
# #     print(123)
# # else:
# #     print(789)
# # try:
# #     a=1+"2"
# #     print(a)
# # except:
# #     print(123)
# # finally:
# #     print(789)
# # try:
# #     a=1+3
# #     print(a)
# # except:
# #     print(123)
# # else:
# #     print(789)
# # finally:
# #     print(9999)
# # import xlwt#调用xlwt模块
# # 创建一个空excel文件
# # f = xlwt.Workbook(encoding="utf-8")
# # 添加一个标写入的单元格，
# # sheet=f.add_sheet("python_test")
# # for i in range(1,10):
# #     for j in range(1,i+1):
# #         sheet.write(i-1,j-1,"{}*{}={}".format(i,j,i*j))
# #保存
# # f.save("ccc.xls")
# # import xlrd
# #打开一个指定文件
# # f = xlrd.open_workbook("ccc.xls")
# #获取要读取的标签也根据索引值来获取
# #sheet=f.sheets()[0]
# #获取有多少个标签
# # b=f.nsheets
# # print(b)
# #根据标签页的名称来获取
# # sheet=f.sheet_by_name("python_test")
# #获取所有标签的名称
# # b = f.sheet_names()
# # print(b)
# #读取某一行内容
# # b=sheet.row_values(1)
# # print(b)
# # c=sheet.nrows
# # for i in range(c):
# #     b=sheet.row_values(i)
# #     print(b)
# # c=sheet.col_values(1)
# # # print(c)
# # b=sheet.cell(1,2).value
# # print(b)
# # for i in range(0,5):
# #     b=sheet.col_values(i)
# #     print(b)
# #将a.txt写入到xxx.xls中
# # import xlwt
# # with open("a.txt","r",encoding="utf-8") as f:
# #         c=[]
# #         a=f.readlines()
# #         for i in a:
# #             i=i.split(",")
# #             c.append(i)
# #         print(c)
# # f=xlwt.Workbook(encoding="utf-8")
# # sheet=f.add_sheet("1")
# # for j in range(len(c)):
# #     for k in range(len(i)):
# #         sheet.write(j,k,c[j][k])
# # f.save("xxx.xls")
#
# # 给excel表格追加内容
# #from xlutils.copy import copy
# # import xlrd
# # f = xlrd.open_workbook("bbb.xls")
#
# #把原有文件复制一份
# # new_f = copy(f)
# #通过索引获取要追加的标签页
# # sheet = new_f.get_sheet(0)
# #写入
# # sheet.write(5,6,"qwdas")
# # f1= xlrd.open_workbook("aaa.xls")
# # new1_f=copy(new_f)
# # sheet1=new1_f.get_sheet(0)
# # sheet.write(15,15,"adsdas")
# # new_f.save("bbb.xls")
#
# #时间模块（自带模块）
# import time
# #时间戳，从公元1970年早上8点到现在经过的秒数
# # a=time.time()
# # print(a)
# #以元组格式默认显示当前时间
# # b=time.localtime(1315546456)
# # print(b)
# #本地化，默认显示当前时间
# # a=time.strftime("%Y-%m-%d %H:%M:%S %w",b)
# # print(a)
# # a=time.strptime("2011-12","%Y-%m")
# # print(a)
# # time.sleep(2)
# #将元组时间转换为时间戳：
# # b=(2012,12,12,12,12,12,3,15,10)
# # a=time.mktime(b)
# # print(a)
# # 判断日期是不是闰年
# # b=input("手动输入一个日期")
# # a=time.strptime(b,"%Y-%m-%d")
# # print(a[0])
# # if b[2]==0 and b[3]==0:
# #     q=a[0]%400
# #     if q==0:
# #         print("是润年")
# #     else:
# #         print("不是闰年")
# # else:
# #     c=a[0]%4
# #     if c==0:
# #         print("是润年")
# #     else:
# #         print("不是闰年")
# # print("星期","{}".format(a[6]+1))
# # print("是今年第",a[7],"天")
# #将b.txt文件追加到xxx.xls中
# # from xlutils.copy import copy
# # import xlrd
# # with open("b.txt","r",encoding="utf-8") as f:
# #         c=[]
# #         a=f.readlines()
# #         for i in a:
# #             i=i.split(",")
# #             c.append(i)
# #         print(c)
# # f1=xlrd.open_workbook("xxx.xls")
# # sheet1=f1.sheets()[0]
# # ac=sheet1.nrows
# # bc=sheet1.ncols
# # new_f1=copy(f1)
# # sheet=new_f1.get_sheet(0)
# # for j in range(len(c)):
# #     for k in range(len(i)):
# #         sheet.write(j+ac,k,c[j][k])
# # new_f1.save("xxx.xls")
#
# # b=input("手动输入一个日期")
# # a=time.strptime(b,"%Y-%m-%d")
# # print(a)
# # a=time.localtime(46546546)
# # print(a)
#
# #打印指定日期前一天的日期
# # b=input("请输入一个日期")
# # # a=time.strptime(b,"%Y-%m-%d")
# # # c=time.mktime(a)
# # # d=c-86400
# # # e=time.localtime(d)
# #  print("{}-{}-{}".format(e[0],e[1],e[2]))
#
# #将ccc.xls内容导入到b.txt中
# # import xlrd
# # f=xlrd.open_workbook("ccc.xls")
# # sheet=f.sheets()[0]
# # c=sheet.nrows
# # with open("b.txt", "w", encoding="utf-8")as h:
# #     for i in range(c):
# #         b=sheet.row_values(i)
# #         print(b)
# #         c=",".join(b)
# #         print(c)
# #         h.write("{}".format(c))
# #         h.write("\n")
#
# # import pymysql
# # import xlrd
# # conn = pymysql.connect(host="192.168.0.68",port=3306,user="root",passwd="1998218")
# # m=conn.cursor()
# # m.execute("use python;")
# # f=xlrd.open_workbook("xxx.xls")
# # sheet=f.sheets()[0]
# # c=sheet.nrows
# # for i in range(c):
# #     b=sheet.row_values(i)
# #      if i==0:
# #         m.execute('create table xxx({} char(20),{} char(20),{} char(20),{} char(20))'.format(b[0],b[1],b[2],b[3]))
# #         m.execute('insert into xxx values("{}","{}","{}","{}")'.format(b[0],b[1],b[2],b[3]))
# # m.execute("select * from xxx")
# # b=m.fetchall()
# # print(b)
#
#
# # m.execute("drop table biao;")
# # m.execute("show tables;")
# # for i in range(30):
# #     m.execute('insert into biao values("小红","{}",{})'.format("女",i))
# # m.execute("select * from biao")
# # b=m.fetchall()
#
# #读取上一个sql语句的结果
#
#
# # print(b)
#
# # import pymysql
# # conn = pymysql.connect(host="192.168.0.68",port=3306,user="root",passwd="1998218")
# # m=conn.cursor()
# # m.execute("use python")
# # with open("a..txt","r",encoding="utf-8") as f:
# #     b=f.readlines()
# # for j in range(len(b)):
# #     c=b[j]
# #     c=c.split(",")
# #     if j==0:
# #         m.execute('create table ccc({} char(255),{} char(255),{} char(255),{} char(255));'.format(c[0], c[1], c[2], c[3]))
# #     m.execute('insert into ccc("{}","{}","{}","{}")'.format(c[0],c[1],c[2],c[3]))
# # m.execute("select * from ccc")
# # x=m.fetchall()
# # print(x)
# # for i in range(len(b)):
# #     c=b[i]
# #     c=c.split(',')
# #     if i==0:
# #         m.execute('create table a({} char(255),{} char(255),{} char(255),{} char(255));'.format(c[0],c[1],c[2],c[3]))
# #     else:
# #         m.execute('insert into a values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
# # m.execute("select * from a")
# # x=m.fetchall()
# # print(x)
#
#
#
#
# #将a.txt文件导入到数据库中
# # import pymysql
# # with open('a.txt','r',encoding='utf-8') as f:
# #     a=f.readlines()
# # noon=pymysql.connect(host='192.168.0.68',port=3306,user='root',passwd='1998218')
# # m=noon.cursor()
# # m.execute('use python')
# # for i in range(len(a)):
# #
# #     c=a[i].split(',')
# #     if i==0:
# #         m.execute('create table lll({} char(255),{} char(255),{} char(255),{} char(255));'.format(c[0],c[1],c[2],c[3]))
# #     else:
# #         m.execute('insert into lll values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
# # m.execute('select * from lll ')
# # d=m.fetchall()
# # print(d)
# # noon.close()
#
# #将数据库导入到Excel表中
# #import pymysql
# # import xlwt
# # coon = pymysql.connect(host='192.168.0.68', port=3306, user='root', passwd='1998218')
# # m=coon.cursor()
# # m.execute("use python")
# # m.execute("desc lll")
# # b=m.fetchall()
# # m.execute("select * from lll")
# # d=m.fetchall()
# # # print(d)
# # f=xlwt.Workbook(encoding="utf-8")
# # sheet=f.add_sheet("python1")
# # for i in range(len(b)):
# #     c=b[i]
# #     sheet.write(0,i,c[0])
# # for j in range(len(d)):
# #     e=d[j]
# #     for k in range(len(e)):
# #         sheet.write(j+1,k,e[k])
# # f.save("shujuku.xls")
#
#
# #将数据库导入到a.txt中
# # import pymysql
# # coon = pymysql.connect(host='192.168.0.68', port=3306, user='root', passwd='1998218')
# # m=coon.cursor()
# # m.execute("use python")
# # m.execute("desc lll")
# # b=m.fetchall()
# # m.execute("select * from lll")
# # d=m.fetchall()
# # print(d)
# # with open("a.txt","w",encoding="utf-8")as f:
# #     for i in range(len(b)):
# #         c=b[i]
# #         f.write("{} ".format(c[0]))
# #     f.write("\n")
# #     for j in range(len(d)):
# #         e=d[j]
# #         for k in range(len(e)):
# #             f.write("{} ".format(e[k]))
#
# #与操作系统交互的模块
# import os
# #获取当前所在位置
# # print(os.getcwd())
# #切换目录
# # os.chdir(r"E:\python")
# # print(os.getcwd)
# #执行cmd命令
# # b=os.popen('route print')
# # print(b.read())
# #获取当前路径下的所有文件
# # print(os.listdir(r"E:\孙跃博的作业"))
# #创建目录
# # os.mkdir("aaa")
# #删除空目录
# # os.rmdir("aaa")
# #创建递归目录
# # os.makedirs(r"a/b/c")
# #删除递归目录
# # os.removedirs(r'a/b/c')
# # 将路径跟文件分隔开
# # b=os.path.split(r"E:\孙跃博的作业")
# # print(b)
# #将后缀名与路径分隔开
# # b=os.path.splitext(r"E:\孙跃博的作业")
# # print(b)
# #判断是否是普通文件
# # b=os.path.isfile(r"E:\孙跃博的作业")
# # print(b)
# #判断是否是目录文件
# # b=os.path.isdir(r"E:\孙跃博的作业")
# #  print(b)
# #删除文件
# # os.remove("a.txt")
#
# #将目录下.py文件打印出来
# # a=os.listdir()
# # for i in a:
# #     b=os.path.isfile(i)
# #     if b==True:
# #         c=os.path.splitext(i)
# #         if c[1]==".py":
# #             print(i)
#
# #封装ssh协议
# import paramiko
# #创建一个ssh客户端
# # ssh123 = paramiko.SSHClient()
# #跳过从know_hosts文件中验证
# # ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #连接
# # ssh123.connect(hostname="192.168.0.68",port=22,username="root",password="1998218")
# #执行命令
# # a,b,c=ssh123.exec_command("ls -al /home")
# #第一个变量：标准输入的命令
# #第二个变量：命令输出
# #第三个变量：是命令的报错
# #
# #读取结果
# # print(b.read().decode())
# #断开连接
# #ssh123.close()
#
# # def ssh(x):
# #     ssh123 = paramiko.SSHClient()
# #     ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #     ssh123.connect(hostname="192.168.0.68", port=22, username="root", password="1998218")
# #     a, b, c = ssh123.exec_command(x)
# #     print(b.read().decode())
# #     return b.read().decode()
# # print(ssh("ls -al /etc"))
#
# #
# #
# # #创建一个传输通道：
# # # qq=paramiko.Transport(("192.168.0.68",22))
# # # qq.connect(username="root",password="1998218")
# # # sftp=paramiko.SFTPClient.from_transport(qq)
# # # sftp.get("/home/a.sh","b.sh")
# # # qq.close()
# #
# # #发送邮件 smtp , pop3 ,imap
# # import smtplib #封装了smtp协议
# # import email.mime.multipart as mul #制作邮件
# # import email.mime.text as text #对文件正文进行处理
# # #创建一个个空邮件
# # message = mul.MIMEMultipart()
# # # 标题
# # message["Subject"]="python_test"
# # # 发件人
# # message["From"]="17629712980@163.com"
# # # 收件人
# # message["To"]="1004745584@qq.com"
# # # 正文
# # txt = """
# # 河南你好
# # 中国你好
# # """
# # # 对正文进行处理
# # tet=text.MIMEText(txt)
# # # 将处理过后的正文添加到邮件里
# # message.attach(tet)
# # # 发送附件
# # att1 = text.MIMEText(open('a.txt', 'rb').read(), 'base64', 'utf-8')
# # att1["Content-Type"] = 'application/octet-stream'
# # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# # att1["Content-Disposition"] = 'attachment; filename="day1.py"'
# # message.attach(att1)
# #
# # # 定义一个邮件服务器
# # smtp123=smtplib.SMTP_SSL("smtp.163.com",465)
# # # 登录服务器 用户名，密码(不是邮箱密码是授权码)
# # smtp123.login("17629712980@163.com","A1998218")
# # # 发送邮件
# # smtp123.sendmail("17629712980@163.com","1004745584@qq.com",message.as_string())
# # # 断开连接
# # smtp123.close()
#
# #socket
# #套接字，提供了通信双方最底层功能
# #pc1 通信 pac2
# # #发送，接收
# # import  socket
# # #创建一个套接字（具有发送和接受能力）
# # #SOCK_STREAM指的是tcp
# # s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # #绑定ip地址和端口号
# # s.bind(("192.168.0.88",3000))
# # #监听
# # s.listen(5)
# # while True:
# #     #接收客户端建立的连接
# #     client,addr=s.accept()
# #
# #         #接受客户端发送的数据
# #     reg=client.recv(1024)
# #     print(reg.decode("utf-8"))
# #     msg=input(">>")
# #         #给客户端发送响应
# #     client.send(msg.encode("utf-8"))
#
# # def a(x,y,z):
# #     # x=list(x)
# #     b=y+z
# #     c=len(x)
# #     if b>c:
# #         b=c
# #     for i in range(y,b):
# #         x.pop(y)
# #     # x=str(x)
# #     print(x)
# # a(["q","w","e"],1,5)
#
# # a="123456"
# # a=list(a)
# # print(a)
#
#
# # def a(x,y):
# #     for i in range(len(x)):
# #         for j in range(i+1,len(x)):
# #            if x[i]+x[j]==y:
# #                print(x[i],x[j])
# # a([1,3,2,2],4)
#
# # import socket
# # #创建一个套接字，SOCK_DGRAM (udp)
# # s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # #绑定ip和端口号
# # s.bind(("192.168.0.88",3000))
# # while True:
# #     #接收客户端的请求
# #     client,addr = s.recvfrom(1024)
# #     print(client.decode("utf-8"))
# #     msg=input(">>>")
# #     s.sendto(msg.encode("utf-8"),addr)
#
# # 正则表达式
# # 匹配文件中的字符串
# import re #将字符串转换为正则表达式
# # a="eeewqeqwewewq1231ewqe"
# # b=re.compile("wq(.*)we",re.S)#将正则表达式编译为python能够识别的正则语言
# # c=b.findall(a)#拿着编译后的正则到字符串中去查找 ，除了查找还有编译功能
# #另一中方法
# # c=re.findall("eq(.*?)wq",a)
# # print(c)
# #替换，将字符串中的某些字符替换其他
# # a=["dasdasdas125456ad","dasdas546546das","dasdas14545das"]
# # for i in a:
# #     c=re.sub("[0-9]+","abc",i)
# #     print(c)
#
# # with open("a.txt","r",encoding="utf-8")as f:
# #     a=f.read()
# # print(a)
#
#
# # a=["13","15"]
# # c="".join(a)
# # print(c)
#
# # print(int(0b1100100))
# # a=chr(97)
# # print(a)
# # a=ord("p")
# # print(a)
# # a=[1,2,5]
# # print(sum(a))
# # a,b=divmod(22020,16)
# # print(a,b)
#
# # import day3
# # day3.sh.a()
#
# # a="asd1sa2d12adas464dsad15465adas"
# # import re
# # b=re.compile("([0-9][0-9]+)")
# # c=b.findall(a)
# # print(c)
# # print(len(c))
#
#
# # a="1123321"
# # a=list(a)
# # c=[i for i in a]
# # c="".join(c)
# # print(c[0])
#
#
# # a="abc123b"
# # b=re.compile("[0-9]+")
# # c=b.findall(a)
# # print(c)
#
# #爬虫 分析网址
# #找到想要的资源并过滤
# #保存
# #对服务器发送请求，将得到的响应数据过滤并保存
# #反爬，防止爬虫程序，批量下载资源
# # import requests
# # import re
# # class FreeBuf():
# #     def send_request(self,c):
# #         url ="https://www.freebuf.com/page/{}".format(c)
# #         head={"user_agent":"Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko"}
# #         #发送请求
# #         res = requests.post(url,headers=head)
# #         #读取结果1.text 以文本的方式接收结果是字符串 2.content 是以字节的方式接收，结果是字节的类型
# #         hh=res.content.decode("utf-8")
# #         return hh
# #
# #     def guolv(self,x):
# #         patt=re.compile('<div class="news-info">(.*?)<dd>',re.S)
# #         itesms=patt.findall(x)
# #         title=[]
# #         for i in itesms:
# #             aa=re.findall('title="(.*?)"',i)
# #             # print(aa)
# #             title.append(aa[0])
# #         return title
# #     def save(self,y):
# #         with open("e.txt","a",encoding="utf-8")as f:
# #             for i in y:
# #                 f.write(i+"\n")
# # #
# # fr =FreeBuf()
# # for i in range(1,5):
# #     # fr.send_request()
# #     xx=fr.send_request(i)
# #     yy=fr.guolv(xx)
# #     fr.save(yy)
#
#
#
# # import requests
# # import re
# # url = 'https://www.qiushibaike.com/imgrank//page/2'
# # head = {
# #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko) Chrome/73.0.3683.103 Safari/537.36'
# #         }
# # res = requests.get(url,headers = head)
# # html = res.content.decode('utf-8')
# # patt = re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg"')#(过滤)
# # itesms = patt.findall(html)
# # print(itesms)
# # a=0
# # for i in itesms:
# #     j = 'https://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
# #     # print(j)
# #     #保存图片 先对图片的连接请求，以字节的方式读取，以字节的方式保存
# #     msg=requests.get(j,headers=head)
# #     hh=msg.content
# #     with open('{}.jpg'.format(a),"wb",)as f:
# #         f.write(hh)
# #     a=a+1
#
#
# # import requests
# # import re
# #
# # url = "https://movie.douban.com/top250?ADUIN=1004745584&ADSESSION=1556523569&ADTAG=CLIENT.QQ.5611_.0&ADPUBNO=26885"
# # res = requests.get(url)
# # html = res.content.decode("utf-8")
# # a = re.compile(
# #     '<img width="100" alt="(.*)" src="https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*).jpg" class="">')
# # b = a.findall(html)
# # print(b)
# #
# #
# # for i in b:
# #     # print(i)
# #     j="https://img{}.doubanio.com/view/photo/s_ratio_poster/public/{}.jpg".format(i[1],i[2])
# #
# #     print(j)
# #     msg=requests.get(j)
# #     hh=msg.content
# #     f=open("{}.jpg".format(i[0]),"wb")
# #     f.write(hh)
# # import json
# # a={"name":"xiaohong"}
# # b=json.dumps(a)
# # c=json.loads(b)
# # print(type(c))
# # a=[1,2,3]
# # b=["a","b","c"]
# # c=list(zip(b,a))
#
#
#
# #web自动化 selenium
# #python代码，控制浏览器打开网页
# #驱动，不同浏览器对应不同驱动
# # from selenium import webdriver
# # from time import sleep
# # dr = webdriver.Firefox()
# #请求要打开的网页
# # dr.get('http://www.baidu.com')
# # sleep(2)
# #打印打开的网页的标题
# # print(dr.title)
# #打印当前网页的网址
# # print(dr.current_url)
# #设置浏览器窗口大小
# # dr.set_window_size(400,400)
# # #设置浏览器的位置
# # dr.set_window_position(400,400)
# #最大化浏览器
# # dr.maximize_window()
# #最小化浏览器
# # dr.minimize_window()
# # dr.get('http://www.jd.com')
# # sleep(2)
# #回退
# # dr.back()
# # sleep(2)
# #前进
# # dr.forward()
# #最重要：定位
# #通过id定位 send_keys(输入) click(点击)
# # dr.find_element_by_id('kw').send_keys('python')
# # sleep(2)
# #点击百度一下
# # dr.find_element_by_id('su').click()
# #通过name定位
# # dr.find_element_by_name('wd').send_keys("python")
# # dr.find_element_by_id('su').click()
# #通过class属性定位
# # dr.find_element_by_class_name('s_ipt').send_keys("python")
# # dr.find_element_by_id('su').click()
# #不论采用任何方式定位，要保证定位的唯一性
# # dr.find_element_by_class_name('mn').click()
# #根据文本定位
# # dr.find_element_by_link_text('新闻').click()
# #模糊定位
# # dr.find_element_by_partial_link_text('hao').click
# #根据标签来定位
# # dr.find_element_by_tag_name()
# #根据路径来定位
# # dr.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/a[1]').click()
# #根据css来定位
# # dr.find_element_by_css_selector('a.mn:nth-child(1)').click()
# # dr.get('http://qzone.qq.com')
# # sleep(2)
# # dr.switch_to.frame('login_frame')0
# # dr.find_element_by_css_selector('#switcher_plogin').click()
# # dr.find_element_by_css_selector('#u').send_keys('1004745584')
# # dr.find_element_by_css_selector('#p').send_keys('SYB.15036785126')
# # dr.find_element_by_css_selector('#login_button').click()
# # def a(x):
# #     y=x+1
# #     return y
# # print(a(1))
# # def a(x):
# #     num=0
# #     for i in range(1,x+1):
# #         num=num+i
# #     return num
# # print(a(100))
# #
# # a=sum(range(1,100))
# # print(a)
#
# import unittest
#unittest写单元测试用的，写断言用的
#按预期结果与实际结果做对比的过程
# class demo(unittest.TestCase):
#     def test_1(self):
#         #假设预期结果是1
#         #实际结果是2
#         #判断预期结果是否等于实际结果
#         a=1 #预期结果
#         #断言：
#         self.assertEqual(a,1)
# if __name__ == '__main__':
#     unittest.main()



from appium import webdriver
from time import sleep
#建立与appium服务器需要的参数，以字典的形式
#TIM
# des={
#   # "device": "android",
#   "platformName": "Android",
#   "platformVersion": "9",
#   "deviceName": "bc0d9588",
#   "appPackage": "com.tencent.tim",
#   "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#   "noReset": "True",
# }
#抖音
# des={
#   "device": "android",
#   "platformName": "Android",
#   "platformVersion": "9",
#   "deviceName": "bc0d9588",
#   "appPackage": "com.ss.android.ugc.aweme",
#   "appActivity": ".main.MainActivity",
#   "noReset": "True",
# }
#测试脚本与appium服务器建立一个session连接
# dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
# # dr.quit()
# sleep(3)
#先清除在输入
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').clear()
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').send_keys('1004745584')
# # dr.find_element_by_id('com.tencent.tim:id/password').clear()
# # dr.find_element_by_id('com.tencent.tim:id/password').send_keys('sunyuebo.1998122')
# # dr.find_element_by_accessibility_id('密码 安全').send_keys('sunyuebo.1998122')
# dr.find_element_by_id('com.tencent.tim:id/password').clear()
# dr.find_element_by_id('com.tencent.tim:id/password').send_keys('SYB.15036785126')
# dr.find_element_by_id('com.tencent.tim:id/login').click()

# dr.find_element_by_id('').find_elements_by_class_name('android.widget.RelativeLayout')
# print(c)
# dr.quit()
# for i in c:
#   sleep(0.5)
#   i.click()
#   sleep(0.5)
# dr.quit()
#获取手机屏幕屏幕大小
# s=dr.get_window_size()
# #放缩x,y轴
# x1=s['width']*0.5
# y1=s['height']*0.25
# y2=s['height']*0.75
# #第三步：使用swipe函数进行活动操作
# while True:
#   dr.swipe(x1,y2,x1,y1)
#   sleep(2)
  # dr.find_element_by_id('com.ss.android.ugc.aweme:id/a2i').click()

# x=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.FrameLayout')
# x[1].click()
# dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
# dr.find_element_by_class_name('android.widget.ImageView').click()


#面向对象：
# class Tim(object):
#   #初始化属性
#   def __int__(self):
#    self.des = {
# #       "device": "android",
# #       "platformName": "Android",
# #       "platformVersion": "9",
# #       "deviceName": "bc0d9588",
# #       "appPackage": "com.tencent.tim",
# #       "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
# #       "noReset": "True",
# #     }
#     self.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des.s)

# from time import sleep
# from appium import webdriver
#
#
#
# # 面向对象
# class Tim(object):
#
#   # 初始化属性
#   def __init__(self):
#     # 建立与appium服务器需要的参数，以字典的形式
#     self.des = {
#       "device": "android",
#       "platformName": "Android",
#       "platformVersion": "9",
#       "deviceName": "bc0d9588",
#       "appPackage": "com.tencent.tim",
#       "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#       "noReset": "true",
#     }
#     # http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
#     # 测试脚本与appium服务器建立一个session连接
#     self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
#     sleep(5)
#
#   def dian_zan(self):
#     # 第一步，点击办公
#     self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[
#       -1].click()
#     # 第二步，点击好友动态
#     t = self.dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name(
#       'android.widget.RelativeLayout')
#     t[-1].click()
#     sleep(0.5)
#     # 第三步 点赞
#     x = self.dr.find_elements_by_class_name('android.widget.ImageView')
#     print(x)
#     x[1].click()
#     sleep(2)
#     x[2].click()
#
#
# # 调用类
# if __name__ == '__main__':
#   yasuo = Tim()
#   yasuo.dian_zan()


  # def get_wenzi(self):
  #   x=self.dr.find_element_by_id('com.tencent.tim:id/ivTitleName').text
  #   print(x)
#   def anjian(self):
#     #模拟人点击物理按键
#     #点击home
#     # self.dr.keyevent(3)
#     # 点击返回键
#     # self.dr.keyevent(4)
#     sleep(10)
#     #拍照键（手动打开箱机）
#     self.dr.keyevent(27)
# if __name__ == '__main__':
#   yasuo = Tim()
#   # yasuo.get_wenzi()
#   yasuo.anjian()


