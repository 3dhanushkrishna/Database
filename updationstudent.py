import sqlite3
connection = sqlite3.connect("college.db")
getRollNumber = input("Enter Roll Number to be updated: ")
getName = input("Enter the New Name: ")
getAdmno = input("Enter the New Admno: ")
getCollege = input("Enter the New College: ")
connection.execute("UPDATE STUDENT SET NAME='"+getName+"',\
ADMNO="+getAdmno+",COLLEGE='"+getCollege+"' WHERE ROLLNUMBER="+getRollNumber)
connection.commit()
print("updated successfully")
result = connection.execute("SELECT * FROM STUDENT")
for i in result:
    print("ID",i[0])
    print("NAME",i[1])
    print("ROLLNUMBER",i[2])
    print("ADMNO",i[3])
    print("COLLEGE",i[4])
