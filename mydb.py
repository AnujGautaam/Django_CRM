# this is for the connection to and management of the database and for the establishment of the connections 
# setting up of the database 

import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    passwd = 'Sunrise111!'
)
# next is the preparation of the cursor object 
cursorObject = dataBase.cursor()


# this is for execution of the cursor object or the creation of the database 
cursorObject.execute("CREATE DATABASE sour")

print("this is the message for the console, and it is all done!")