lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]

first_none_pos = None
all_nones_pos = []
for i, item in enumerate(lst_data):
    if item is None:
        if first_none_pos is None:
            first_none_pos = i
        all_nones_pos.append(i)

print('First None position: ', first_none_pos)
print('All None positions: ', all_nones_pos)
            