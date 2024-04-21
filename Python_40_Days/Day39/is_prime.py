def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
if __name__ == '__main__':
    numbers = [-1, 0.5, 1, 2, 3, 5, 8, 13, 21, 34, 'blah']
    for num in numbers:
        print(f'{num} is prime: {is_prime(num)}')
    print(is_prime.__annotations__)