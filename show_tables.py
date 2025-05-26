import mysql.connector

nama_db = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_connect',
}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

kursor.execute("SHOW TABLES")

for(table_name, ) in kursor:
    print(table_name)