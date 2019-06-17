import random
#注意：这里的元素下标是从0开始的；若把数组从小到大排序，第k小的元素在数组中（k+1）的位置。
def KthMin(arr, n):
    return __kmin(arr, 0, len(arr) - 1, n)

def __kmin(arr, l, r, n):
    if r==l:
        return arr[l]
    j = __partition(arr, l, r)
    if n < j:
        return __kmin(arr, l, j - 1,n)
    elif n > j:
        return __kmin(arr, j + 1, r,n)
    else: # n == j
        return arr[j]

# 返回j，使得 arr[l,1,2,...j-1]< arr[j] < arr[j+1,.....r]
def __partition(arr, l, r):
    t = random.randint(l, r)
    arr[l], arr[t] = arr[t], arr[l]
    j = l
    # arr[l+1,.....j] <arr[l] < arr[j+1,....i)
    for i in range(l + 1, r + 1):
        if arr[i] < arr[l]:
            arr[i], arr[j + 1] = arr[j + 1], arr[i]
            j += 1
    arr[l], arr[j] = arr[j], arr[l]
    return j
arr = [8,6,2,3,1,5,7,4]
print(KthMin(arr, 3))