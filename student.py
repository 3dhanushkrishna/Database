import sqlite3
connection = sqlite3.connect("college.db")
# connection.execute('''CREATE TABLE STUDENT(
#                       ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                       NAME TEXT,
#                       ROLLNUMBER INTEGER,
#                       ADMNO INTEGER,
#                       COLLEGE TEXT
# );  ''')

print("Table Created Successfully")

getName = input("Enter Name: ")
getRollNumber = input("Enter RollNumber: ")
getAdmno = input("Enter AdmnoNumber: ")
getCollege = input("Enter College name: ")
connection.execute("INSERT INTO STUDENT(NAME,ROLLNUMBER,ADMNO,COLLEGE) \
VALUES('"+getName+"',"+getRollNumber+","+getAdmno+",'"+getCollege+"')")
connection.commit()
connection.close()
print("Inserted Successfully")