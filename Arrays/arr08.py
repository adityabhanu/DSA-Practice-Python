# Maximum even numbers present in any subarray of size K
arr = [0, 1, 4, 5, 1, 6]
K = 3

maxCount = 0
for i in range(K):
    if arr[i] % 2 == 0:
        maxCount += 1
l = 1
r = K
count = maxCount
while(r < len(arr)):

    if arr[r] % 2 == 0:
        count += 1
    if arr[l-1] % 2 == 0:
        count -= 1

    maxCount = max(maxCount, count)

    l += 1
    r += 1

print(maxCount)
