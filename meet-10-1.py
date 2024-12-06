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

# execute -> buat Query
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS mahasiswa (
        id INT,
        nama VARCHAR(100),
        npm INT(10))
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
    INSERT INTO mahasiswa (npm, nama, id)
    VALUES
        (5210411135, "Widi", 1),
        (5210411136, "Widi", 2),
        (5210411137, "Widi", 3),
        (5210411138, "Widi", 4),
        (5210411139, "Widi", 5),
        (5210411133, "Widi", 6),
        (5210411132, "Widi", 7)
"""
)

# menjalankan Query
conn.commit()

# menutup koneksi
conn.close()
