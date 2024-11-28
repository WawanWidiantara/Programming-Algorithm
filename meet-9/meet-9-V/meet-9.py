# # Dictionary {} -> "key" -> matematika, "value" -> ilmu yang mempelajari ...
# mahasiswa = {
#     "nama": "Widi",
#     "npm": 134,
#     "alamat": "jl",
#     "asal": "Bali",
# }

# # # Cara mengambil data dictionary
# # ? langsung
# print(f"Pemanggilan secara langsung: {mahasiswa['nama']}")
# # ? dengan get() -> get(key, default value if not found)
# print(mahasiswa.get("ip", "Key not found"))

# # Cara mengupdate/insert data
# #! key "ip" val 4
# # secara langsung
# mahasiswa["ip"] = 4
# mahasiswa["ip"] = 3
# print(mahasiswa)

# # dengan update()
# mahasiswa.update({"ip": 4})
# mahasiswa.update({"ip": 3})
# print(mahasiswa)

# # menghapus data dictionary
# # dengan del
# del mahasiswa["nama"]
# print(mahasiswa)
# # dengan pop
# mahasiswa.pop("alamat")
# print(mahasiswa)
# # menghilangkan nilai terakhir
# mahasiswa.popitem()
# print(mahasiswa)

key_lain = {
    0: "nama",
}

print(key_lain)

# angka = 1
# str(angka)

contoh_tuple = (1, 2, 3)
print(type(list(contoh_tuple)))
