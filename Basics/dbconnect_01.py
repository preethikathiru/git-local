import datetime;
import mysql.connector
from env import host

def printtime():
    ct = datetime.datetime.now()
    return ct

s=printtime()
print("start:",s)

def queryexe():
    cnx = mysql.connector.connect(user='preethika', password='preethika',host=host,
                              database='preethika',port=3306)
    mycursor = cnx.cursor()
    mycursor.execute("select * from detail1")
    result=mycursor.fetchall()
    for i in result:
        print(i)
    cnx.close()

x=queryexe()

e=printtime()
print("end:",e)

def difftime():
    dt=e-s
    return dt

result=difftime()
print("difference:",result)

