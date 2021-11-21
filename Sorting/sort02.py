# Bubble Sort
# kind of opposite of selection sort, after every
# iteration we will get the highest element placed at the end
# compare adjacent elements

arr = [2, 6, 4, 0, 1]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
