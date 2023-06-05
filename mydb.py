import mysql.connector

dataBase = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd= 'r3dil&pa55'

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE redil")

print ("All Done!")