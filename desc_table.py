import mysql.connector

nama_db = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_connect',
}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

kursor.execute("DESC siswa")

for (column) in kursor:
    print(column[0]),
    print(column[1]),
    