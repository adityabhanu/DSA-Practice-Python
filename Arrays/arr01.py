# Shift all 0's at the end of an array

arr = [0,1,2,0,3,4,0]

idx = 0
for i in range(0, len(arr)):
    if arr[i] != 0:
        arr[idx] = arr[i]
        idx+=1

while(idx < len(arr)):
    arr[idx] = 0
    idx += 1

print(arr)