def interpolate(arr, method='nearest_neighbor'):
    res = []
    for i, item in enumerate(arr):
        if item:
            res.append(item)
        else:
            prev_item = next_item = None
            prev_dist = next_dist = float('inf')

            # Search backward
            for j in range(i - 1, -1, -1):
                if arr[j]:
                    prev_item = arr[j]
                    prev_dist = i - j
                    break
            
            # Search forward
            for j in range(i + 1, len(arr)):
                if arr[j]:
                    next_item = arr[j]
                    next_dist = j - i
                    break
            
            if prev_item and next_item:
                if method == 'nearest_neighbor':
                    interpolated_item = prev_item if prev_dist <= next_dist else next_item
                elif method == 'linear':
                    '''
                    f(x) = (y2-y1)/(x2-x1)*(x-x1) + y1,
                    where (y2-y1)/(x2-x1) is slope,
                        (x-x1) is prev_dist,
                        (x2-x1) is next_dist + prev_dist,
                        y1 is prev_item
                    '''
                    slope = (next_item - prev_item) / (next_dist + prev_dist)
                    interpolated_item = slope * prev_dist + prev_item
            elif prev_item:
                interpolated_item = prev_item
            elif next_item:
                interpolated_item = next_item
            else:
                interpolated_item = None
            res.append(interpolated_item)
    return res

lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]
print('Original array:\n', lst_data)
print('Nearest neighbor interpolation:\n', interpolate(lst_data, method='nearest_neighbor'))
print('Linear Interpolation:\n', interpolate(lst_data, method='linear'))

lst_data = [None, None, None, None, 3.5, None, 2.5, None]
print('\nOriginal array:\n', lst_data)
print('Nearest neighbor interpolation:\n', interpolate(lst_data, method='nearest_neighbor'))
print('Linear interpolation:\n', interpolate(lst_data, method='linear'))

lst_data = [2.0, 2.2, None, 2.7, None, 4.9, 6.2, None]
print('\nOriginal array:\n', lst_data)
print('Nearest neighbor interpolation:\n', interpolate(lst_data, method='nearest_neighbor'))
print('Linear interpolation:\n', interpolate(lst_data, method='linear'))