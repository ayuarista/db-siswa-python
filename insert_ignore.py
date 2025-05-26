import mysql.connector

nama_db = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_connect',
}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

kursor.execute("""INSERT IGNORE INTO siswa (id, nama, alamat, telepon) VALUES
(1, 'John Doe', '123 Main St', '1234567890'),
(2, 'Jane Smith', '456 Elm St', '0987654321'),
(3, 'Alice Johnson', '789 Oak St', '5551234567'),
(4, 'Bob Brown', '321 Pine St', '5559876543'),
(5, 'Charlie Black', '654 Maple St', '5555555555');""")

koneksi.commit()

print("Data telah berhasil ditambahkan")
koneksi.close()

