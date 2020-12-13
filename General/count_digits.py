def count_digit(num):
    if num == 0:
        return 0
    return 1 + count_digit(num // 10)


if __name__ == '__main__':
    num = 123
    res = count_digit(num)
    print(f'Number of digits in the {num} :', res)
