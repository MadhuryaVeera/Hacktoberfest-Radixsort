def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(9):
        count[i + 1] += count[i]

    i = 0  # ❌ Wrong direction — should go from end to start for stability
    while i < n:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i += 1

    for i in range(len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))  # Expected [2, 24, 45, 66, 75, 90, 170, 802]
