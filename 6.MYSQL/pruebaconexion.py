from debugpy import connect
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="secret")

mycursor = mydb.cursor()

