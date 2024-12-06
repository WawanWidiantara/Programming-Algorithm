import sqlite3

# Membuat atau membuka database
conn = sqlite3.connect('./db/db2/my_database.db')
cursor = conn.cursor()
cursor.execute("""
            CREATE TABLE IF NOT EXISTS pengguna (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nama TEXT NOT NULL, 
                usia INTEGER,
                email TEXT UNIQUE
            )
            """)
conn.commit()
conn.close()

# # Memasukan data ke tabel
# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()
# cursor.execute("""
#                 INSERT INTO pengguna (nama, usia, email)
#                 VALUES ('asep', 17, 'asep@gmail.com')
#             """)
# conn.commit()
# conn.close()

# # inputan pengguna
# nama = input('Inputkan Nama Anda: ')
# usia = input('Inputkan Usia Anda: ')
# email = input('Inputkan Email Anda: ')

# # Memasukan data ke tabel
# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()

# query = """
#             INSERT INTO pengguna (nama, usia, email)
#             VALUES (?, ?, ?)
#         """
# values = (nama, usia, email)
# cursor.execute(query, values)

# conn.commit()
# conn.close()

# Memasukan data ke tabel
conn = sqlite3.connect('./db/db2/my_database.db')
cursor = conn.cursor()

query = """
            INSERT INTO pengguna (nama, usia, email)
            VALUES (?, ?, ?)
        """
values = [
    ('asep', 17, 'asep@gmail.com'),
    ('agus', 20, 'agus@gmail.com'),
    ('ujang', 23, 'ujang@gmail.com')
]
cursor.executemany(query, values)

conn.commit()
conn.close()

# # Mengambil data
# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()

# query = "SELECT * FROM pengguna WHERE usia>15"
# cursor.execute(query)
# data_pengguna = cursor.fetchall()

# for pengguna in data_pengguna:
#     print(pengguna)

# cursor.close()

# # Memperbarui data
# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()

# query = """
#             UPDATE pengguna
#             SET nama='Asep Senang'
#             WHERE id=1
#         """
# cursor.execute(query)

# query_tampil = "SELECT * FROM pengguna"
# cursor.execute(query_tampil)
# data_pengguna = cursor.fetchall()

# for pengguna in data_pengguna:
#     print(pengguna)

# conn.commit()
# conn.close()


# # Memperbarui data dari inputan user
# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()

# # inputan pengguna
# nama = input('Inputkan Nama Anda: ')
# usia = input('Inputkan Usia Anda: ')
# email = input('Inputkan Email Anda: ')
# id_pengguna = input('Inputkan ID pennguna Anda: ')

# query = """
#             UPDATE pengguna
#             SET nama=?, usia=?, email=?
#             WHERE id=?
#         """
# values = (nama, usia, email, id_pengguna)
# cursor.execute(query, values)

# query_tampil = "SELECT * FROM pengguna"
# cursor.execute(query_tampil)
# data_pengguna = cursor.fetchall()

# for pengguna in data_pengguna:
#     print(pengguna)

# conn.commit()
# conn.close()


# # Memperbarui data dari inputan user
# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()

# query = "DELETE FROM pengguna WHERE id=2"
# cursor.execute(query)

# query_tampil = "SELECT * FROM pengguna"
# cursor.execute(query_tampil)
# data_pengguna = cursor.fetchall()

# for pengguna in data_pengguna:
#     print(pengguna)

# conn.commit()
# conn.close()

# # Memperbarui data dari inputan user
# conn = sqlite3.connect('my_database.db')
# cursor = conn.cursor()

# id_pengguna = input("masukan id pengguna: ")

# query = "DELETE FROM pengguna WHERE id=?"
# values = (id_pengguna)
# cursor.execute(query, values)

# query_tampil = "SELECT * FROM pengguna"
# cursor.execute(query_tampil)
# data_pengguna = cursor.fetchall()

# for pengguna in data_pengguna:
#     print(pengguna)

# conn.commit()
# conn.close()
