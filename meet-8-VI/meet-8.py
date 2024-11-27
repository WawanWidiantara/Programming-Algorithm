# List, Tuple & Set, Dictionary

#? List/Array -> []
#? Index -> urutan dimulai 0
#? Length -> panjang list / jumlah value yang ada di dalamnya
#! Tipe data: int, str, float, bool
angka = 1
nama = "Widi"
ip = 4.0
is_mahasiswa = True

list_angka = [1,"Widi", 4.0, True,3,1,1,2,3,234,43,443,"Ini"]
index_terakhir = list_angka[-1]
#! Ketika length list = 4
#! Maka max index len - 1 = 3
print(f"Panjang list angka: {len(list_angka)}")
print(f"Index ke-1 dari belakang: {list_angka[-1]}")

#? Buat list yang di dalamnya berisikan angka genap yang kurang dari sama dengan 20 dengan nama variable "list_genap"

    #! masukkan nilai ke-3 dari list_genap kedalam variable "index_3"

    #! masukkan nilai ke 4 dari belakang pada list_genap ke dalam variable "index_min_4"
    
    #! Jumlahkan "index_3" dan "index_min_4"
 
    #! Tampilkan ke output:
        #? panjang list
        #? index_3
        #? index_min_4
        #? hasil penjumlahan

list_genap = [2,4,6,8,10,12,14,16,18,20]
index_3 = list_genap[2]
index_min_4 = list_genap[-4]
jumlah = index_3 + index_min_4
print(f"Panjang list: {len(list_genap)}") 
print(f"Index ke 3: {index_3}") 
print(f"Index min 4: {index_min_4}") 
print(f"Hasil penjumlahan: {jumlah}") 