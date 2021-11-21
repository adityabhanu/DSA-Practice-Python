# find count of all the subarrays with sum 5 and length 3
# ans = 2

arr = [1,2,3,0,5,1,23,0,4,1]
count = 0
for i in range(0, len(arr)):
    sum = 0
    length = 0
    for j in range(i, len(arr)):
        sum = sum + arr[j]
        length+=1
        if sum == 5 and length == 3:
            count = count+1

print(count)

