#用归并算法的思想 求逆序对儿
def ReverseOrder(arr):
    return reverseOrder(arr, 0, len(arr) - 1)

def reverseOrder(arr, l, r):
    mid = l + (r - l) // 2
    if l >= r:
        return 0
    if l < r:
        count1 = reverseOrder(arr, l, mid)
        count2 = reverseOrder(arr, mid + 1, r)

        return count1 + count2 + merge(arr, l, r, mid)

def merge(arr, l, r, mid):
    count = 0
    i = l
    j = mid + 1
    temp = [None] * (r - l + 1)
    for k in range(r - l + 1):
        if j > r: # 如果右半部分的元素已处理完毕
            temp[k] = arr[i]
            i += 1
        elif i > mid: # 如果左半部分的元素已处理完毕
            temp[k] = arr[j]
            j += 1
        elif arr[i] <= arr[j]: #左半部分的元素 < 右半部分的元素
            temp[k] = arr[i]
            i += 1

        elif arr[j] < arr[i]: # 右半部分的元素 < 左半部分的元素
            temp[k] = arr[j]
            j += 1
            # 此时, 因为右半部分j所指的元素小
            # 这个元素和左半部分的所有未处理的元素都构成了逆序数对
            # 左半部分此时未处理的元素个数为 mid - i + 1
            count += mid - i + 1

    arr[l:r + 1] = temp
    return count
#N*(N-1)/2
arr = [8,7,6,5,4,3,2,1]
print(ReverseOrder(arr))