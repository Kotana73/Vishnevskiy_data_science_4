n_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
dct = {}
for j in n_list:
    if j in dct:
        dct[j] += 1
    else:
        dct[j] = 1
result = [el for el in n_list if dct[el] == 1]
print(result)