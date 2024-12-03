list_genap = [2,4,6,8,10,12,14,16,18,20]
# Index ke-0 : 2
# Index ke-1 : 4
# Index ke-2 : 6
# ...
# Index ke-9 : 20

# cara 1 - value
for value in list_genap:
    print(f"Index ke: {value}")

# cara 2 - index
list_genap[5]
for i in range(len(list_genap)):
    # print(i) # 0, 1, ..., 9
    print(f"Index ke-{i}: {list_genap[i]}")

# cara 3 - index & value
for i, value in enumerate(list_genap): # (0, 2)
    print(f"Index ke-{i}: {value}")
    
