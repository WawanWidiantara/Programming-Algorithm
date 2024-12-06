# Database
# ? Bedanya dengan List & dkk -> Bisa disimpan tanpa harus dijalankan programnya
# list_angka = [0, 12, 3, 4]
# print(list_angka[0])

#! Database -> Tabel -> Colomn -> Row (data)
#! Query -> Perintah
# #! Step:
# 1. Membuat koneksi ke database
# 2. Membuat cursor -> untuk query
# 3. Membuat Query dengan cursor
# 4. Menjalankan perintah
# 5. Tutup Koneksi

import sqlite3

# membuat koneksi
conn = sqlite3.connect("db/uty.db")
cursor = conn.cursor()

# execute -> buat Query -> PRIMARY KEY
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS mahasiswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama VARCHAR(100) NOT NULL,
        npm INT(10) NOT NULL
        )
"""
)

# menjalankan Query
conn.commit()

# menutup koneksi
conn.close()

#! Memasukkan data ke database
# membuat koneksi
conn = sqlite3.connect("db/uty.db")
cursor = conn.cursor()

# execute -> masukkan data
# SYNTAX
"""
    INSERT INTO nama_table (kolom1, kolom2)
    VALUES
        (nilai1, nilai2)
"""
cursor.execute(
    """
    INSERT INTO mahasiswa (nama, npm)
    VALUES
        ("Widi", 5210411135),
        ("Widi", 5210411135)
"""
)

# menjalankan Query
conn.commit()

# menutup koneksi
conn.close()
