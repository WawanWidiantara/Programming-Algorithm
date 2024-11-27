# List
#! List Manipulation

# Mengubah value
list_nama = ["Widi", "Antara", "Ilham"] # "Charles"
print(f"Sebelum diubah: {list_nama}")
list_nama[1] = "Dean"
print(f"Setelah diubah: {list_nama}")
print("="*100)

# Menambahkan/Menginput Value Baru
#! Append -> Inputkan value baru di paling belakang
print(f"Sebelum append: {list_nama}")
list_nama.append("Charles")
print(f"Setelah append: {list_nama}")
print("="*100)
#! Insert -> Inputkan value baru sesuai index yang diinginkan
print(f"Sebelum insert: {list_nama}")
list_nama.insert(1, "Daniel")
print(f"Setelah insert: {list_nama}")
print("="*100)

# Menghapus Value
#! Pop -> Menghapus yang paling terakhir
print(f"Sebelum pop: {list_nama}")
list_nama.pop()
print(f"Setelah pop: {list_nama}")
print("="*100)
#! Remove -> Menghapus nilai yang spesifik
print(f"Sebelum remove: {list_nama}")
list_nama.remove("Widi")
print(f"Setelah remove: {list_nama}")
print("="*100)

# Mengurutkan Value
list_angka = [0,1,21,53,21,1,3,8,3,3,3,12,4,4,4,4,8,9]
#! Ascending
print(f"Sebelum sort: {list_angka}")
list_angka.sort()
print(f"Setelah sort: {list_angka}")
print("="*100)
#! Descending
print(f"Sebelum reverse: {list_angka}")
list_angka.reverse()
print(f"Setelah reverse: {list_angka}")
print("="*100)

# Count -> menghitung
print(f"Jumlah angka 3: {list_angka.count(3)}")

# Penggabungan
list_nama_tambahan = ["Antara", "Abdillah"]
#! Extend
print(f"Sebelum extend: {list_nama}")
list_nama.extend(list_nama_tambahan)
print(f"Setelah extend: {list_nama}")
print("="*100)
#! operator "+"
print(f"Sebelum tambah: {list_nama}")
list_nama = list_nama + list_nama_tambahan
print(f"Setelah tambah: {list_nama}")
print("="*100)

#! cara menghapus sekaligus
list_delete = ["Daniel", "Dean"]
for value in list_delete:
    list_nama.remove(value)
print(f"Setelah tambah: {list_nama}")