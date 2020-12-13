def trailing_zero(num):
    res = 0
    i = 5
    while i <= num:
        res += num // 5
        i *= 5
    return res


if __name__ == '__main__':
    num = 5
    res = trailing_zero(num)
    print(f'Trailing no of zeros in factorial of {num} :', res)
