# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end="\t")
#     print()

# a="123"
# b=a[::-1]
# c=0
# for i in range(len(a)):
#     for j in range(10):
#         if b[i]==str(j):
#             c=c+j*10**i
# print(c)

# import os
# # os.mkdir('aaa')
# with open('a.txt','w',encoding='utf-8')as f:
#     for i in range(10):
#         f.write("asdsa"+"\n")


# import pymysql
# with open('a..txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# noon=pymysql.connect(host='192.168.0.200',port=3306,user='root',passwd='123456')
# m=noon.cursor()
# m.execute('use test')
# for i in range(len(a)):
#
#     c=a[i].split(',')
#     if i==0:
#         m.execute('create table uuu({} char(255),{} char(255),{} char(255),{} char(255));'.format(c[0],c[1],c[2],c[3]))
#     else:
#         m.execute('insert into uuu values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
# m.execute('select * from uuu ')
# d=m.fetchall()
# print(d)
# noon.close()


# import  socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(("192.168.0.68",3000))
# s.listen(5)
# while True:
#     client,addr=s.accept()
#     reg=client.recv(1024)
#     print(reg.decode("utf-8"))
#     msg=input(">>")
#     client.send(msg.encode("utf-8"))


# import requests
# import xlwt
# import json
# url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&=0&_v=0.26795321&x-zp-page-request-id=099e722d6fd746daac0801b591fb6dad-1557223432774-720202'
# head = {
#          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko) Chrome/73.0.3683.103 Safari/537.36'
#         }
# a=requests.get(url,head)
# b=a.content.decode('utf-8')
# c=json.loads(b)
# d=[]
# for i in range(90):
#     d.append([c['data']['results'][i]['jobName'],c['data']['results'][i]['eduLevel']['name'],c['data']['results'][i]['company']['name'],c['data']['results'][i]['salary'],c['data']['results'][i]['company']['size']['name']])
#
# f=xlwt.Workbook(encoding="utf-8")
# sheet=f.add_sheet("1")
# # print(d)
# for i in range(len(d)):
#     for j in range(len(d[i])):
#         sheet.write(i,j,d[i][j])
# f.save("ccc.xls")
#
# import pymysql
# noon=pymysql.connect(host='192.168.0.78',port=3306,user='root',passwd='1998218')


