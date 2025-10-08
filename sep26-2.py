import sqlite3

con=sqlite3.connect('users.db')
print(con)

cur=con.cursor()

cur.execute('create table if not exists user(user_id int,name text,email text,age int)')

#cur.execute("insert into user values(100,'manu','manu@gmail.com',22)")
# no=int(input('Enter the number of users that you want to enter :'))
# for i in range(1,no+1):
#     print('User :',i)
#     userid=int(input('Enter the user_id of the user:'))
#     name=input('Enter the name of the user :')
#     email=input('Enter the email of the user :')
#     age=int(input('Enter the age of the user :'))
#     cur.execute('insert into user values(?,?,?,?)',(userid,name,email,age))
#     con.commit()
# con.commit()

cur.execute('select * from user')
data=cur.fetchall()
print('{:<10}{:<10}{:<20}{:<10}'.format('UserId','Name','Email','Age'))
print('-'*50)
for i in data:
    print('{:<10}{:<10}{:<20}{:<10}'.format(i[0],i[1],i[2],i[3]))

cur.execute('select name,age from user where age>=200')
data1=cur.fetchall()
for i in data1:
    print(i)