# # # # # Database
# # # # # ? Bedanya dengan List & dkk -> Bisa disimpan tanpa harus dijalankan programnya
# # # # # list_angka = [0, 12, 3, 4]
# # # # # print(list_angka[0])

# # # # #! Database -> Tabel -> Colomn -> Row (data)
# # # # #! Query -> Perintah
# # # # # #! Step:
# # # # # 1. Membuat koneksi ke database
# # # # # 2. Membuat cursor -> untuk query
# # # # # 3. Membuat Query dengan cursor
# # # # # 4. Menjalankan perintah
# # # # # 5. Tutup Koneksi

# # # import sqlite3

# # # # # membuat koneksi
# # # # conn = sqlite3.connect("db/uty.db")
# # # # cursor = conn.cursor()

# # # # # execute -> buat Query -> PRIMARY KEY
# # # # cursor.execute(
# # # #     """
# # # #     CREATE TABLE IF NOT EXISTS mahasiswa (
# # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # #         nama VARCHAR(100) NOT NULL,
# # # #         npm INT(10) NOT NULL
# # # #         )
# # # # """
# # # # )

# # # # # menjalankan Query
# # # # conn.commit()

# # # # # menutup koneksi
# # # # conn.close()

# # # # #! Memasukkan data ke database
# # # # # membuat koneksi
# # # # conn = sqlite3.connect("db/uty.db")
# # # # cursor = conn.cursor()

# # # # # execute -> masukkan data
# # # # # SYNTAX
# # # # """
# # # #     INSERT INTO nama_table (kolom1, kolom2)
# # # #     VALUES
# # # #         (nilai1, nilai2)
# # # # """
# # # # cursor.execute(
# # # #     """
# # # #     INSERT INTO mahasiswa (nama, npm)
# # # #     VALUES
# # # #         ("Widi", 5210411135),
# # # #         ("Ilham", 5210411101)
# # # # """
# # # # )

# # # # # menjalankan Query
# # # # conn.commit()

# # # # # menutup koneksi
# # # # conn.close()

# # # # Mengambil data dari database
# # # # membuat koneksi
# # # conn = sqlite3.connect("db/uty.db")
# # # cursor = conn.cursor()

# # # cursor.execute("""SELECT * FROM mahasiswa""")
# # # list_mahasiswa = cursor.fetchall()
# # # print("before update")
# # # for mahasiswa in list_mahasiswa:
# # #     print(mahasiswa)

# # # cursor.execute(
# # #     """
# # #     UPDATE mahasiswa
# # #     SET npm = 135
# # #     WHERE id = 1
# # # """
# # # )
# # # conn.commit()

# # # cursor.execute("""SELECT * FROM mahasiswa""")
# # # list_mahasiswa = cursor.fetchall()
# # # print("after update")
# # # for mahasiswa in list_mahasiswa:
# # #     print(mahasiswa)

# # # conn.close()


# # import sqlite3

# # conn = sqlite3.connect("db/uty.db")
# # cursor = conn.cursor()

# # cursor.execute(
# #     """
# #     DELETE FROM mahasiswa
# #     WHERE id = 1
# # """
# # )

# # conn.commit()
# # conn.close()

# import sqlite3

# conn = sqlite3.connect("db/uty.db")
# cursor = conn.cursor()

# nama = input("Inputkan nama: ")
# npm = int(input("Inputkan npm: "))

# cursor.execute(
#     """
#         INSERT INTO mahasiswa (nama, npm)
#         VALUES (?,?)
# """,
#     (nama, npm),
# )

# conn.commit()
# conn.close()

