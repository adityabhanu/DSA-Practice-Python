# Print sum of all subarrays of size K
# Think of sliding window first
arr = [2, 6, 4, 0, 1]
K = 3


def sumSubArr(arr, n, K):
    l = 0
    r = K - 1
    sum = 0
    for i in range(K):
        sum += arr[i]
    print(sum)

    while(r+1 < n):
        sum = sum - arr[l+1] + arr[r]
        print(sum)
        l += 1
        r += 1


sumSubArr(arr, len(arr), K)
