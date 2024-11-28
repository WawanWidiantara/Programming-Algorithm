# nested dictionary

mahasiswa = {
    "MH001": {
        "nama": "Widi",
        "npm": 135,
    },
    "MH002": {
        "nama": "Ilham",
        "npm": 101,
    },
}

# get "Ilham"
# print(mahasiswa["MH002"]["nama"])

# Widi, Ilham

# items()
for item in mahasiswa.items():
    print(item)
    print(item[1]["nama"])

# keys()
for item in mahasiswa.keys():  # -> MH001, MH002
    print(item)
    print(mahasiswa[item]["nama"])

# values()
for item in mahasiswa.values():
    print(item)
    print(item["nama"])

print(f"Tipe items(): {type(mahasiswa.items())}")
print(f"Tipe keys(): {type(mahasiswa.keys())}")
print(f"Tipe values(): {type(mahasiswa.values())}")
