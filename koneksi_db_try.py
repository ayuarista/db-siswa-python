import mysql.connector
from mysql.connector import errorcode

try:
    koneksi = mysql.connector.connect(user='root', host='localhost', password='', database='db_connect')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Koneksi berhasil")