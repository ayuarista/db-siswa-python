import mysql.connector

nama_db = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_connect',
}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

kursor.execute(
    """INSERT INTO siswa (id, nama, alamat) VALUES (1, 'John Doe', '123 Main St');"""
)
koneksi.commit()
print("Data telah berhasil ditambahkan")

koneksi.close()