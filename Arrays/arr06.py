# Find max of all subarrays of size K
# subarrays of size K => always think of sliding window approach once
# But in this case sliding window will not help

arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
K = 4


def maxSubArr(arr, K):
    maxArr = []
    for i in range(0, len(arr)-K+1):
        maxVal = arr[i]
        for j in range(i+1, i+K):
            if maxVal < arr[j]:
                maxVal = arr[j]
        maxArr.append(maxVal)
    return maxArr


maxSubArrayList = maxSubArr(arr, K)
print(maxSubArrayList)
