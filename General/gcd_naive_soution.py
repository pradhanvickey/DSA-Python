def gcd(num1, num2):
    num = min(num1, num2)
    while num > 0:
        if num1 % num == 0 and num2 % num == 0:
            break
        num -= 1
    return num


if __name__ == '__main__':
    num1, num2 = 5, 10
    res = gcd(num1, num2)
    print(f'HCF of {num1} and {num2} : ', res)
