# NSR | Nearest Smaller to Right
# complexity: o(n)

def nearest_smaller_to_right(arr, size):
    stack = []
    res = []

    for i in range(size, -1, -1):
        found = -1
        while len(stack) > 0:
            value = stack[-1]
            if arr[i] > value:
                res.append(value)
                stack.append(arr[i])
                found = 1
                break
            else:
                stack.pop()

        if found == -1:
            res.append(-1)
            stack.append(arr[i])
    res.reverse()
    print(res)


if __name__ == '__main__':
    arr = [1, 3, 2, 5]
    size = len(arr) - 1
    nearest_smaller_to_right(arr, size)
