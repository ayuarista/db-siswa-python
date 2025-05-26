import mysql.connector
nama_db = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_connect',
}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()
kursor.execute("""CREATE TABLE siswa(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    alamat VARCHAR(100),
    telepon VARCHAR(15)
    );
""")
koneksi.commit()
print("Tabel siswa berhasil dibuat")
koneksi.close()
# Kode ini membuat tabel siswa dengan kolom id, nama, alamat, dan telepon.
