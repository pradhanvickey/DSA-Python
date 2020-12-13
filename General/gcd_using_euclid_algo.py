def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


if __name__ == '__main__':
    num1, num2 = 10, 14
    res = gcd(num1, num2)
    print(f'HCF of {num1} and {num2} : ', res)
