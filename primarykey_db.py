import mysql.connector

nama_db = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_connect',
}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

kursor.execute("""ALTER TABLE siswa ADD PRIMARY KEY (id);""")
koneksi.commit()

for (column) in kursor:
    print(column[0]),
    print(column[1]),
    print(column[2]),
    print(column[3]),
koneksi.close()