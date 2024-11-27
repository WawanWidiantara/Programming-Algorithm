# List, Tuple & Set, Dictionary

#? List / Array [index -> 0, length]
list_genap = [2,4,6,8,10]

panjang_list_genap = len(list_genap)
index_3 = list_genap[3] #! mengambil nilai index ke-
index_terakhir = list_genap[-1] #! (-) digunakan untuk mengambil index terakhir

print(f"Tipe data: {type(list_genap)}")
print(f"Panjang list: {panjang_list_genap}")
print(f"Index ke-3: {index_3}")
print(f"Index terakhir: {index_terakhir}")

# ini list genap index ke-0: nilai
# ini list genap index ke-1: nilai
# ini list genap index ke-2: nilai
# ini list genap index ke-3: nilai
# ini list genap index ke-4: nilai
# ini list genap index ke-5: nilai

# cara 1 {nilai}
for nilai in list_genap:
    print(f"ini nilai: {nilai}")

# cara 2 {index}
for i in range(0, len(list_genap)):
    # print(i) #! i = 0,1,2,3,4
    print(f"ini nilai: {list_genap[i]}")

# cara 3 {index & nilai}
for index, value in enumerate(list_genap):
    print(f"ini list genap index ke-{index}: {value}")