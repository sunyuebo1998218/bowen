# b=os.path.split(r"路径")#将路径跟文件分隔开
# b=os.path.splitext(r"路径")#将后缀名跟文件分隔开
# print(os.get(wd()))#获取当前位置
# print(os.listdir())获取当前位置的下的所有文件
# os.chdir("切换路径")
# b=os.popen("cmd mingling")#执行cmd命令
# print(b.read())读取出来
# os.mkdir("aaa")创建文件夹 os.rmdir("aaa')：删除 ，os.makedirs("lujing”）
# os.removedirs(r"aaa/bbb/ccc")
# b=os.path.isfile(r"路径")
# b=os.path.isdir(r"lujing")
# class Shuxue:
#     def a(self):
#         print("help")
#     def c(self):
#         print("123")

# sh=Shuxue()
# # # sh.a()
# class qwe():
#     def __a(self):
#         print("qeqwascsa")
#     def c(self):
#         print("87897")
#         self.__a()
# q=qwe()
# q.c()
# class qwe():
#     def __init__(self,name,xueliang):
#         self.name=name
#         self.xueliang=xueliang
#     def asd(self):
#         self.xueliang -= 200
#         print("{},还剩下{}".format(self.name,self.xueliang))
#     def zxc(self):
#         self.xueliang += 500
#         print("{},还剩余{}".format(self.name,self.xueliang))
# q=qwe('小明',1000)
# w=qwe('李白',2000)
# q.asd()

import paramiko
# ssh123=paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname="192.168.0.68",port=22,username="root",password="1998218")
# a,b,c=ssh123.exec_command("ls -al /home")
# #第一个变量a:标准输入的命令
# #第二个变量b：命令的输出结果
# #第三个变量c：是命令的报错
#
# #读取命令输出的结果
# print(b.read().decode())
# ssh123.close()

# qq=paramiko.Transport(("192.168.0.68",22))
# qq.connect(username="root",password="1998218")
# sftp=paramiko.SFTPClient.from_transport(qq)
# sftp.get("/home/a.sh","b.sh")
# sftp.put("day1.py","/etc/day1.py")
# qq.close()


# import smtplib
# import email.mime.multipart as mul
# import email.mime.text as text
# message=mul.MIMEMultipart()
# message["subject"]="python_test"
# message["From"]="17629712980@163.com"
# message["To"]="1004745584@qq.com"
# txt="""
#     饭饭
#     蛋蛋
# """
# tet=text.MIMEText(txt)
# message.attach(tet)
# smtp123=smtplib.SMTP_SSL("smtp.163.com",465)
# smtp123.login("17629712980@163.com","A1998218")
# smtp123.sendmail("17629712980@163.com","1004745584@qq.com",message.as_string())
# smtp123.close()