def is_palindrome(num):
    rev_num = 0
    temp = num
    while temp > 0:
        rev_num = (rev_num * 10) + temp % 10
        temp = temp // 10
    if rev_num == num:
        return True
    return False


if __name__ == '__main__':
    num = 101
    result = is_palindrome(num)
    print(f'Is {num} palindrome: ', result)
