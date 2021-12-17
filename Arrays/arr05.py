# Rain water tapping problem
# find total water that can be trapped, each array value reprents height of the pillar
# width of all pillars = 1

arr = [3, 0, 2, 0, 4]
# arr = [1, 2, 3, 3, 2, 1]

# find how much water each pillar is holding

# for a pillar to store, it should have higher pillar on both sides

# but smaller pillar will decide how much water will be stored

# to compute this we need highest bar in the right and highest bar in the left

# contribution of each pillar = min(max right, max left) - pillar height

# use prefix sum, but here store max of 0 -> i


preMaxLeft = [0 for i in range(len(arr))]

preMaxRight = [0 for i in range(len(arr))]


def prefixMaxLeft(arr, n, preMaxLeft):
    preMaxLeft[0] = arr[0]

    for i in range(1, n):
        preMaxLeft[i] = max(arr[i], preMaxLeft[i-1])


def prefixMaxRight(arr, n, preMaxRight):
    preMaxRight[len(arr)-1] = arr[len(arr) - 1]

    for i in range(len(arr) - 2, -1, -1):
        preMaxRight[i] = max(preMaxRight[i+1], arr[i])


prefixMaxLeft(arr, len(arr), preMaxLeft)

prefixMaxRight(arr, len(arr), preMaxRight)

sum = 0
for i in range(0, len(arr)):
    sum = sum + min(preMaxLeft[i], preMaxRight[i]) - arr[i]

print(sum)
