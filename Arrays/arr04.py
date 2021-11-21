# Prefix Sum = summation of all elements from 0->i
# Sum of all elements from 0 -> i = prefix(i)

arr = [2, 6, 4, 0, 1]


ps = [0 for i in range(len(arr))]


def prefixSum(arr, n, ps):
    ps[0] = arr[0]

    for i in range(1, n):
        ps[i] = arr[i] + ps[i-1]


prefixSum(arr, len(arr), ps)


print(ps)

"""
[2, 6, 4, 0, 1] => [2, 8, 12, 12, 13]

Note: Usage of this concept:
if we have to find array sum between index l and r, 
instead of running a loop from l to r,
we can find the sum between l->r as prefixSum(r) - prefixSum(l)

sum(l,r) = sum(0,r) - sum(0,l-1)
sum(l,r) = prefix(r) - prefix(l-1)
 
"""
