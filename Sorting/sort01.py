# Selection Sort

arr = [2, 6, 4, 0, 1]

for i in range(len(arr)):
    minValIdx = i
    for j in range(i, len(arr)):
        if arr[j] < arr[minValIdx]:
            minValIdx = j
    arr[i], arr[minValIdx] = arr[minValIdx], arr[i]

print(arr)
