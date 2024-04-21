import numpy as np

def quadratic_equation(a, b, c):
    print(f'\na = {a}, b = {b}, c = {c}')
    if a == 0:
        if b == 0:
            return 'No solution'
        return f'The root is x = {-c / b}'
        
    delta = b**2 - 4 * a * c
    if delta < 0:
        return 'No solution'
    elif delta == 0:
        return f'The double root is x1 = x2 = {-b / (2 * a)}'
    else:
        x1 = (-b + np.sqrt(delta)) / (2 * a)
        x2 = (-b - np.sqrt(delta)) / (2 * a)
        return f'The roots are x1 = {x1}, and x2 = {x2}'

print(quadratic_equation(2, 6, 4))
print(quadratic_equation(1, 2, 1))
print(quadratic_equation(4, 6, 3))
print(quadratic_equation(0, 2, -4))
print(quadratic_equation(0, 0, 4))
    

    

