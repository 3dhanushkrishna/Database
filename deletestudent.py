import sqlite3
connection = sqlite3.connect("college.db")
getRollNumber = input("Enter Roll Number to be deleted: ")
connection.execute("DELETE FROM STUDENT WHERE ROLLNUMBER="+getRollNumber)
connection.commit()
print("Deleted Successfully")
result = connection.execute("SELECT * FROM STUDENT")
for i in result:
    print("ID",i[0])
    print("NAME",i[1])
    print("ROLLNUMBER",i[2])
    print("ADMNO",i[3])
    print("COLLEGE",i[4])
