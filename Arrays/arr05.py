# Rain water tapping problem
# find total water that can be trapped, each array value reprents height of the pillar
# width of all pillars = 1

arr = [3, 0, 2, 1, 0, 4]

# find how much water each pillar is holding

# for a pillar to store, it should have higher pillar on both sides

# but smaller pillar will decide how much water will be stored

# contribution of each pillar = min(max right, max left) - pillar height

# use prefix sum, but here store max of 0 -> i

ps = [0 for i in range(len(arr))]


def prefixSum(arr, n, ps):
    ps[0] = arr[0]

    for i in range(1, n):
        ps[i] = max(arr[i], ps[i-1])


prefixSum(arr, len(arr), ps)

sum = 0
for i in range(len(arr)):
    sum = sum + min(ps[i-1], ps[len(arr) - 1]) - arr[i]

print(sum)
