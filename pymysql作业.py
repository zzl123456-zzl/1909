import  pymysql

conn=pymysql.Connect(host="127.0.0.1",user="root",password="123",db='bbs',port=3306,charset='utf8')
coursor=conn.cursor()
#创建数据库和表

try:
  coursor.execute("creat database bbs default charset=utf8")
  coursor.execute("creat table user(uid int pyrimary key auto_increment, username varchar(50) union,usertype enum(0,1) default 0,password ,regtime datetime ,email varchar(100)) ")
  #插入成员信息
  username=input("请输入用户名")
  usertype=input("请输入用户类型1或者0")
  password=input("请输入密码")
  email=input("请输入个人邮箱")
  coursor.execute("insert into username(username,usertype,password,email) values('{}','{}','{}','{}')").format(username,usertype,password,email)
except Exception as  e:
    conn.rollback()
finally:
    coursor.close()
    conn.close()

#用户登录

import  pymysql
conn=pymysql.Connect(host="127.0.0.1",user="root",password="123",db='bbs',port=3306,charset='utf8')
coursor=conn.cursor()
try:
  username=input("请输入用户名")
  password=input("请输入密码")
  data=coursor.execute("select uid from user where username='{}'and password='{}'").format(username,password)
  if data:
      print("登录成功")
  else:
      print("密码错误，请重新输入")
  coursor.execute("select username,usertype,password,regtime,email from user")

except Exception as  e:
    conn.rollback()
finally:
    coursor.close()
    conn.close()

