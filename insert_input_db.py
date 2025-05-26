from datetime import date
import mysql.connector

data_aset = {}

id_siswa = input("Masukkan id: ")
nama_siswa = input("Masukkan nama: ")
alamat_siswa = input("Masukkan alamat: ")
telepon_siswa = input("Masukkan telepon: ")

data_aset['id'] = id_siswa
data_aset['nama'] = nama_siswa
data_aset['alamat'] = alamat_siswa
data_aset['telepon'] = telepon_siswa

nama_db = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_connect',
}

try:
    koneksi = mysql.connector.connect(**nama_db)
    kursor = koneksi.cursor()
    
    tambah_db = ("INSERT INTO siswa (id, nama, alamat, telepon) "
                 "VALUES (%(id)s, %(nama)s, %(alamat)s, %(telepon)s)")
    kursor.execute(tambah_db, data_aset)
    koneksi.commit()
    
    print("Data berhasil dimasukkan")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    
finally:
    if koneksi.is_connected():
        kursor.close()
        koneksi.close()
