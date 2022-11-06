from hashlib import sha1
import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',password='',db='pj01',charset='utf-8')
name = input('User Name')
password = input('Password')
res = [name]

pwd2 = sha1(pwd.encode('utf-8')).hexdigest()

sql = 'select password from userinfo where name=%s'
cus1=conn.cursor()
cus1.execute(sql,res)
pwd = cus1.fetchall()

if psw==():
    print('User Name Unknow.')
elif psw[0][0]==pwd2:
    print('Sucessful')
else:
    print('Password is wrong.')
conn.commit()
cus1.close()
conn.close()