import copy

# Operasi List
list_awal = [1, 8, 2, 4, 7, 4, 3, 5, 2]


def add_tiga(data):
    list_awal = data.copy()
    #! menjumlahkan setiap value dalam list dengan 3
    # code disini

    return list_awal


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
    customer = copy.deepcopy(data)
    #! tambahkan ke customer
    # {
    #     "CUST003": {
    #         "nama": "Ali",
    #         "wallet": 50000,
    #     },
    # }
    # code disini

    return customer


print(add_data(customer))
print(add_tiga(list_awal))


#! print waktu saat ini