import copy

# Operasi List
list_awal = [1, 8, 2, 4, 7, 4, 3, 5, 2]


def add_tiga(data):
    dataset = data.copy()
    #! menjumlahkan setiap value dalam list dengan 3
    # code disini

    return dataset


# Operasi Dictionary
customer = {
    "CUST001": {
        "nama": "Widi",
        "wallet": 10000,
    },
    "CUST002": {
        "nama": "Ilham",
        "wallet": 10000,
    },
}


def add_data(data):
    dataset = copy.deepcopy(data)
    #! tambahkan ke dataset
    # {
    #     "CUST003": {
    #         "nama": "Ali",
    #         "wallet": 50000,
    #     },
    # }
    # code disini

    return dataset


print(add_data(customer))


#! print waktu saat ini
