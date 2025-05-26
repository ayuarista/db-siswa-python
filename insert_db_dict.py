from datetime import date 
import mysql.connector

data_aset = {
    'id': '10001',
    'nama': 'Nishimura Niki',
    'alamat': 'Tokyo',
    'telepon': '1234567890',
}

nama_db = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_connect'
}

try:
    koneksi = mysql.connector.connect(**nama_db)
    kursor = koneksi.cursor()
    
    tambah_db = ("INSERT INTO siswa (nama, alamat, telepon) "
                 "VALUES (%(nama)s, %(alamat)s, %(telepon)s)")
    kursor.execute(tambah_db, data_aset)
    koneksi.commit()
    
    print("Data berhasil dimasukkan")
    
except mysql.connector.Error as err:
    print(f"Error: {err}")
    
finally:
    if koneksi.is_connected():
        kursor.close()
        koneksi.close()