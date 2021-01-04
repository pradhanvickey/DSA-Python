def binary_search(arr, start, end, num):
    if start <= end:
        mid = start + (end - start) // 2
        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
        return binary_search(arr, start, end, num)
    else:
        return -1


if __name__ == '__main__':
    arr = list(range(0, 10))
    num = 5
    res = binary_search(arr, 0, len(arr) - 1, num)
    print("Index: ", res)
