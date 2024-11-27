# # Manipulasi List = []
# list_nama = ["Widi", "Antara", "Ilham"]
# #? Memasukkan/Menambahkan nilai ke list
# #! Append
# print(f"list sebelum append {list_nama}")
# list_nama.append("Dean")
# print(f"list sesudah append {list_nama}")
# print("="*100)
# #! Insert
# print(f"list sebelum insert {list_nama}")
# list_nama.insert(1, "Ali")
# print(f"list setelah insert {list_nama}")
# print("="*100)
# #! Extend
# list_nama_2 = ["Romli", "Made", "Putu"]
# print(f"list sebelum extend {list_nama}")
# list_nama.extend(list_nama_2)
# print(f"list setelah extend {list_nama}")

# #? Menghapus nilai dari list
# #! Pop
# print(f"list sebelum pop {list_nama}")
# list_nama.pop()
# print(f"list setelah pop {list_nama}")
# print("="*100)
# #! Remove {berdasarkan value}
# print(f"list sebelum remove {list_nama}")
# list_nama.remove("Ali")
# print(f"list setelah remove {list_nama}")
# print("="*100)

# list_angka = [1,5,2,6,8,2,3,3,1,3,3,3,3,3,3,3,3]
# print(f"penggunaan index: {list_angka.index(2)}")
# print(f"penggunaan count: {list_angka.count(3)}")
# print(f"sebelum penggunaan sort: {list_angka}")
# list_angka.sort()
# print(f"setelah penggunaan sort: {list_angka}")
# print(f"sebelum penggunaan sort: {list_angka}")
# list_angka.reverse()
# print(f"setelah penggunaan sort: {list_angka}")

#! Slicing
list_angka = [1,5,2,6,8,2,3,3,1,3,3,3,3,3,3,3,3]
# list_baru = list angka yang sampai index ke 10
awal = 5
akhir = 9
list_baru = list_angka[awal:akhir]
print(list_baru)
