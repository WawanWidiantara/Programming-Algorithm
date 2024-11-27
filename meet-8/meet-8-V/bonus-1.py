# Bonus 21/11/'24

#? Buat list yang berisikan angka ganjil kurang dari 15
    #! masukkan index ke-2 ke variabel "index_2"
    #! masukkan index terakhir ke-4 ke variabel "index_min"
    #! jumlahkan index_2 dan index_min
    #! tampilkan ke output:
        #? panjang list
        #? index_2
        #? index_min
        #? hasil

# list_ganjil = [1,3,5,7,9,11,13]
list_ganjil = range(1,15,2)
panjang_list_ganjil = len(list_ganjil)
index_2 = list_ganjil[2]
index_min = list_ganjil[-4]
hasil = index_2 + index_min
print(f"Tipe data: {type(list_ganjil)}")
print(f"Panjang list: {panjang_list_ganjil}")
print(f"Index ke-3: {index_2}")
print(f"Index terakhir: {index_min}")