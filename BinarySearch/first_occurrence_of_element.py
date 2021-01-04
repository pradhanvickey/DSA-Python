def first_occurrence(arr, size, num):
    start = 0
    end = size - 1
    res = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == num:
            res = mid
            end = mid - 1
        elif arr[mid] > num:
            end = mid - 1
        else:
            start = start + 1
    return res


if __name__ == '__main__':
    arr = [1, 2, 2, 2, 5, 5, 5, 5]
    num = 2
    res = first_occurrence(arr, len(arr), num)
    print("Index: ", res)
