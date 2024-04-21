# 1
lst_data = [i for i in range(1, 13) if not i % 2]
print(lst_data)

# 2
for num in lst_data:
    if num % 3 == 0:
        lst_data.remove(num)
print(lst_data)

# 3
lst_data.extend(range(1, 4))
lst_data[3:3] = range(6, 9)
print(lst_data)

# 4
for i in range(len(lst_data)):
    if lst_data[i] % 2 == 0 or lst_data[i] % 5 == 0:
        lst_data[i] = 0
print(lst_data)
