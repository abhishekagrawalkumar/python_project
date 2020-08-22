import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Abhishek@123",database="first")
#print(mydb)

mycursor = mydb.cursor()
out=int(input("Press 1 for SIGN-UP and 2 for SIGN-IN :) "))
if(out==1):
  e_mail=input("your Email-id :) ")
  password=input("Choose your Password :) ")
  sql = "INSERT INTO customers (email, pass) VALUES (%s, %s)"
  val = (e_mail, password)
  mycursor.execute(sql, val)

  mydb.commit()
  print()
  print("THANK YOU FOR CONNECTING WITH US :)")
if(out==2):
  e_mail=input("Enter  your Email-id :) ")
  password=input("Enter your Password :) ")
  sql = "SELECT pass FROM customers WHERE email= %s"
  e=(e_mail, )
  mycursor.execute(sql, e)
  myresult = mycursor.fetchall()
  print()
  if(password==myresult[0][0]):
    print("LOGIN SUCCESSFUL")
  else:
    print("LOGIN FAILED")

  

#mycursor.execute("CREATE TABLE Customers (email VARCHAR(50), pass VARCHAR(50))")
#mycursor.execute("SHOW TABLES")
#for x in mycursor:
#  print(x)shdghj

'''import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Abhishek@123"
)

print(mydb)'''
