# Kadane's Algorithm
# Find largest sum contiguous sub array

arr = [-2, -3, 10, -8, 2, 15, -16]
# trick is whenever you get negative sum start from zero again

# maxSum = 0
# for i in range(0, len(arr)):
#     sum = 0
#     for j in range(i, len(arr)):
#         sum = sum+arr[j]
#         if sum < 0:
#             break
#         if sum > maxSum:
#             maxSum = sum

# print(maxSum)

maxSum = 0
sum = 0

for i in range(0, len(arr)):
    sum = sum + arr[i]
    if sum < 0:
        sum = 0
    if sum > maxSum:
        maxSum = sum

print(maxSum)
