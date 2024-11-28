# Quiz V
#! Menghapus list yang memiliki nilai lebih dari 5
# ? input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#! Konversi tuple ke dalam list, kemudian tambahkan nilai yang ada di dalam list dengan nilai 10, lalu konversi kembali kedalam tuple
# ? input_tuple = (1, 2, 3, 4, 5)

#! Menambahkan umur setiap orang dengan 13 dalam bentuk dictionary
# ? input_dict = {'John': 10, 'Jane': 12, 'Jessica': 11}

# Quiz V
#! Menambahkan setiap nilai list dengan 5
#! Menghapus nilai dalam dictionary dan menambahkan nilai baru

# Tantangan 1: Menghapus nilai lebih dari 5 dari sebuah list
# Input: List berisi integer
# Output: List dengan nilai lebih dari 5 dihapus


def hapus_nilai_lebih_dari_lima(input_list):
    """
    Fungsi untuk menghapus semua nilai yang lebih besar dari 5 dari list input.

    Parameter:
    - input_list (list of int): List berisi angka-angka.

    Mengembalikan:
    - list: List baru yang hanya berisi nilai <= 5 dari input_list.
    """
    # Implementasikan kode Anda di sini
    for i in input_list:
        if i > 5:
            input_list.remove(i)
    return input_list


# Tantangan 2: Konversi tuple ke dalam list, tambahkan nilai 10 pada setiap elemen,
# kemudian konversi kembali ke dalam tuple
# Input: Tuple berisi integer
# Output: Tuple dengan setiap elemen bertambah 10


def konversi_dan_tambah(input_tuple):
    """
    Fungsi untuk mengubah tuple menjadi list, menambahkan 10 pada setiap elemen, dan mengubahnya kembali menjadi tuple.

    Parameter:
    - input_tuple (tuple of int): Tuple berisi angka-angka.

    Mengembalikan:
    - tuple: Tuple baru dengan setiap elemen bertambah 10.
    """
    # Implementasikan kode Anda di sini
    input_tuple = list(input_tuple)
    for i in range(len(input_tuple)):
        input_tuple[i] += 10
    return tuple(input_tuple)


# Tantangan 3: Menambahkan umur setiap orang dengan 13 dalam bentuk dictionary
# Input: Dictionary dengan kunci nama (str) dan nilai umur (int)
# Output: Dictionary dengan umur yang sudah ditambah 13


def tambah_umur_13(input_dict):
    """
    Fungsi untuk menambahkan 13 tahun pada setiap umur orang dalam dictionary.

    Parameter:
    - input_dict (dict): Dictionary dengan nama sebagai kunci dan umur sebagai nilai.

    Mengembalikan:
    - dict: Dictionary baru dengan setiap umur ditambah 13.
    """
    # Implementasikan kode Anda di sini
    pass


# Kasus uji untuk memeriksa solusi
def uji_hapus_nilai_lebih_dari_lima():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_output = [1, 2, 3, 4, 5]
    try:
        assert (
            hapus_nilai_lebih_dari_lima(input_list) == expected_output
        ), "Test 1 Gagal"
        print("Test 1 Berhasil!")
    except AssertionError as e:
        print(f"{e}")


def uji_konversi_dan_tambah():
    input_tuple = (1, 2, 3, 4, 5)
    expected_output = (11, 12, 13, 14, 15)
    try:
        assert konversi_dan_tambah(input_tuple) == expected_output, "Test 2 Gagal"
        print("Test 2 Berhasil!")
    except AssertionError as e:
        print(f"{e}")


def uji_tambah_umur_13():
    input_dict = {"John": 10, "Jane": 12, "Jessica": 11}
    expected_output = {"John": 23, "Jane": 25, "Jessica": 24}
    try:
        assert tambah_umur_13(input_dict) == expected_output, "Test 3 Gagal"
        print("Test 3 Berhasil!")
    except AssertionError as e:
        print(f"{e}")


# Fungsi utama untuk menjalankan pengujian
if __name__ == "__main__":
    uji_hapus_nilai_lebih_dari_lima()
    uji_konversi_dan_tambah()
    uji_tambah_umur_13()
