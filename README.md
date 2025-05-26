# 🐍 Python MySQL - Database Siswa

Project ini menggunakan Python dan `mysql.connector` untuk membangun dan mengelola database MySQL, pada tabel **siswa**. Berisi berbagai query yang mencakup koneksi, pembuatan tabel, dan operasi data siswa.

## 🧩 Modul yang Tersedia

| File Python           | Fungsi                                                                 |
|------------------------|------------------------------------------------------------------------|
| `Koneksi_db.py`        | Membuat koneksi awal ke database MySQL                                |
| `Koneksi_db_try.py`    | Versi koneksi dengan error handling menggunakan `try-except`          |
| `Create_table.py`      | Membuat tabel `siswa` di database                                     |
| `Primarykey_db.py`     | Menambahkan primary key ke tabel                                      |
| `Insert_db.py`         | Menambahkan data siswa ke tabel                                       |
| `Insert_input_db.py`   | Input data siswa dari user dan simpan ke database                     |
| `Insert_db_dict.py`    | Menambahkan data siswa menggunakan dictionary Python                  |
| `Insert_ignore_db.py`  | Menambahkan data siswa dengan `INSERT IGNORE`                         |
| `Desc_table.py`        | Menampilkan struktur tabel dengan `DESC`                              |
| `Show_tables.py`       | Menampilkan semua tabel di database                                   |

## 🛠️ Library yang Digunakan

- `mysql-connector-python`

## 📦 Instalasi

1. **Clone repository**
   ```bash
   https://github.com/ayuarista/db-siswa-python
   cd db-siswa-python
