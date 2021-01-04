def binary_search(arr, size, num):
    start = 0
    end = size - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == '__main__':
    arr = list(range(0, 10))
    res = binary_search(arr, len(arr), -5)
    print("Index: ", res)