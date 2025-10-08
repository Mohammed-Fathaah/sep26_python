import sqlite3

con=sqlite3.connect('users.db')
print(con)

cur=con.cursor()

cur.execute('create table if not exists user(user_id int,name text,email text,age int)')

#cur.execute("insert into user values(100,'manu','manu@gmail.com',22)")
no=int(input('Enter the number of users that you want to enter :'))
for i in range(1,no+1):
    print('User :',i)
    userid=int(input('Enter the user_id of the user:'))
    name=input('Enter the name of the user :')
    email=input('Enter the email of the user :')
    age=int(input('Enter the age of the user :'))
    cur.execute('insert into user values(?,?,?,?)',(userid,name,email,age))
    con.commit()
con.commit()