def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)


if __name__ == '__main__':
    num = 5
    res = factorial(num)
    print(f'Factorial of {num} :', res)
