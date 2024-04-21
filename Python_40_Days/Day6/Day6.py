time = input('Input time: ')

# Method 1
if time == '6 AM':
    print('Snooze...')
elif time == '6:08 AM':
    print('Let\'s sleep a litte more')
elif time == '9 AM':
    print('Oh I\'m dead')
else:
    print('Do something else')

# Method 2
todo = {'6 AM': 'Snooze...', 
        '6:08 AM': 'Let\'s sleep a litte more',     
        '9 AM': 'Oh I\'m dead'}
print(todo.get(time, 'Do something else'))

# Method 3
match time:
    case '6 AM':
        print('Snooze...')
    case '6:08 AM':
        print('Let\'s sleep a litte more')
    case '9 AM':
        print('Oh I\'m dead')
    case _:
        print('Do something else')