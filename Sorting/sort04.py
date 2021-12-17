# Count Sort
# Solved using an array

arr = [2, 6, 4, 0, 1, 2, 6, 2]


def countSort(arr, n):

    freqArr = [0 for i in range(10)]

    for i in range(n):
        freqArr[arr[i]] += 1

    idx = 0
    for i in range(len(freqArr)):
        while freqArr[i] > 0:
            arr[idx] = i
            idx += 1
            freqArr[i] -= 1

    return arr


sortedArr = countSort(arr, len(arr))
print(sortedArr)
