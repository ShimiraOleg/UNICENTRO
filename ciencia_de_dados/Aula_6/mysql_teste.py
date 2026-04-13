import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(host='localhost',
                              user='root',
                              password='mateus#73',
                              database='loja_teste')


cursor = cnx.cursor()
cursor.execute("SELECT * FROM clientes")

for row in cursor.fetchall():
    print(row)

cnx.close()