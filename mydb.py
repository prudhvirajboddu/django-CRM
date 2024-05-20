import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

cursorobject = database.cursor()

cursorobject.execute(" CREATE DATABASE djangodb")

print('Done!')