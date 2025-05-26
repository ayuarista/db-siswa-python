import mysql.connector

nama_db = {
    'user': 'root',
    'password': '',
    'database': 'db_connect',
}

koneksi = mysql.connector.connect(**nama_db)
print("koneksi telah berhasil dilakukan")
koneksi.close