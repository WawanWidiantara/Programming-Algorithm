# Slicing -> memotong -> ":" -> [awal:akhir]
list_genap = [2,4,6,8,10,12,14,16,18,20]
list_setelah_10 = list_genap[5:] # [12,14,16,18,20]
list_sebelum_10 = list_genap[:3] # [2,4,6,8]

list_antara = list_genap[2:8] # [6,8,10,12,14,16,18]
# or
list_antara = list_genap[2:-2] # [6,8,10,12,14,16,18]

# print(list_genap)
# print(list_setelah_10)
# print(list_sebelum_10)
# print(list_antara)

# output: value -> awal = 4, akhir = 7
for value in list_genap[:]:
    print("output: ",value)
