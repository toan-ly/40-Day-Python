shopping_list = ['Ca rot', 'Tao', 'Sua']

# Method 1
print('Shopping list:')
for i in range(len(shopping_list)):
    print(f'{i + 1}. {shopping_list[i]}')
    
# Method 2
print('\nShopping list:')
for i, item in enumerate(shopping_list, start=1):
    print(f'{i}. {item}')
    
    
food_list = [['Bo', 'Pizza', 'Sua'], 
             ['Xuc xich', 'Tao', 'Kem'],
             ['Ca rot', 'Banh dau', 'Cupcake']]

search_items = ['Ca rot', 'Tao', 'Sua']

# Method 1
print()
for i in range(len(food_list)):
    for j in range(len(food_list[i])):
        if food_list[i][j] in search_items:
            print(f'{food_list[i][j]} is found '
                  f'at row {i + 1} and column {j + 1}.')
            
# Method 2
print()
for i, row in enumerate(food_list, start=1):
    for j, item in enumerate(row, start=1):
        if item in search_items:
            print(f'{item} is found '
                  f'at row {i} and column {j}.')
        