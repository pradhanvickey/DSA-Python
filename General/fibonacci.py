def fibo(num):
    a = 0
    b = 1
    while num > 0:
        print(a, end=" ")
        a, b = b, a + b
        num -= 1


if __name__ == '__main__':
    fibo(5)
