# 1
lst_data = list(range(1, 11))
print(lst_data)

# 2
def find_median(lst_data):
    n = len(lst_data)
    if n % 2:
        return lst_data[n//2]
    return (lst_data[n//2 - 1] + lst_data[n//2]) / 2

lst_data.sort()
print('Median: ', find_median(lst_data))

# 3
lst_odd_filter = [i for i in lst_data if i % 2]
lst_odd_filter.sort(reverse=True)
print(lst_odd_filter)