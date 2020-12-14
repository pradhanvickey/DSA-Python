def prime_factor(num):
    if num <= 0:
        print("Not a prime")
    i = 2
    while i * i <= num:
        while num % i == 0:
            print(i)
            num = num // 2
        i += 1
    if num > 1:
        print(num)


if __name__ == '__main__':
    num = 8
    prime_factor(num)
