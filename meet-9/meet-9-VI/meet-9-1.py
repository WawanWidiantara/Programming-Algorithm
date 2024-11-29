# Dictionary
# ? Struktur Data yang menampung 'key' dan 'value'
# ? {key: value}
# ? index -> key
# ? Apakah key = str ?? -> int str bool float
# ? Apakah value harus 1?? -> bebas

mahasiswa = {
    "nama": "Widi",
    "npm": 135,
    "asal": "Bali",
}

# Mengambil data pada dictionary
#! secara langsung
print(mahasiswa["npm"])
# print(mahasiswa["ip"]) #! should be error

#! dengan get()
print(f"Dengan get(): {mahasiswa.get('npm')}")
print(f"Dengan get('ip'): {mahasiswa.get('ip')}")
print(f"Dengan get('ip'), dengan default: {mahasiswa.get('ip','Key not found')}")

