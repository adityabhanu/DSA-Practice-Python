# Insertion Sort
# insert an element in a sorted array without removing ascending property

arr = [2, 6, 4, 0, 1]


def insertionSort(arr, n):
    for i in range(1, n):
        valueToSort = arr[i]

        j = i-1

        while j >= 0 and arr[j] > valueToSort:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = valueToSort

    return arr


sortedArr = insertionSort(arr, len(arr))
print(sortedArr)
