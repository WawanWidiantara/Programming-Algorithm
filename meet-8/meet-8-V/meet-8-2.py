# Nested List
list_data_siswa = ["Widi", 135, 4.0] # 1D
list_kumpulan_siswa = [
    ["Widi", 135, 4.0],
    ["Antara", 136, 4.0],
    ["Ilham", 101, 4.0],
    ["Dean", 102, 4.0],
] # 2D

# Output = "Widi"
list_luar = list_kumpulan_siswa[0] # ['Widi', 135, 4.0]
list_dalam = list_luar[0] # "Widi"
print(list_kumpulan_siswa[0][0])