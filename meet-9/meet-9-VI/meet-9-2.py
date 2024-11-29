# operasi .keys(), .values(), .items()
mahasiswa = {
    "nama": "Widi",
    "npm": 135,
    "asal": "Bali",
    "ip": 4.0,
}

# ? keys()
print(f"Keys: {mahasiswa.keys()}")
#! Menampilkan semua values di mahasiswa
for key in mahasiswa.keys():
    print(f"Value: {mahasiswa[key]}")
print("=" * 50)

# ? values()
print(f"Values: {mahasiswa.values()}")
for value in mahasiswa.values():
    print(f"Value: {value}")
print("=" * 50)

# ? nested dictionary
mahasiswas = {
    "MH001": {
        "nama": "Widi",
        "npm": 135,
        "asal": "Bali",
        "ip": 4.0,
    },
    "MH002": {
        "nama": "Ilham",
        "npm": 101,
        "asal": "Ciamis",
        "ip": 4.0,
    },
}
for item in mahasiswas.items():
    # cara mengurangi ip -1
    item[1]["ip"] -= 1  # -> item[1]["ip"] = item[1]["ip"] - 1
    print(item[1])

customer = {
    "John": 24,  # -> 34
    "Michael": 17,  # -> 27
    "Albert": 30,  # -> 40
}

# menambah semua umur +10
#! loop
for key in customer.keys():
    customer[key] += 10
print(customer)

list_angka = [2, 4, 6, 8, 10]  # -> [1,3,5,7,9]
for i in range(len(list_angka)):
    list_angka[i] -= 1
print(list_angka)
