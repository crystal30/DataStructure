
def binarySearch(arr, target):

    '''
    :param arr: 有序的数组
    :param target: 需要找的目标值
    :return: 返回目标值所在的位置
    '''

    len_arr = len(arr)

    # 在[left...right]的范围内寻找 target
    left = 0
    right = len_arr - 1
    # n = (right + left) // 2  # 注意：这句话要写正确，不是(right - left) // 2
    n = left + (right - left)//2 # 防止整型溢处 
    while left <= right:  # 当left == right 时，[left...right] 依然有效
        if arr[n] > target:
            right = n-1

        elif arr[n] < target:
            left = n+1

        else:
            return n

        n = (right - left) // 2

    return -1 # target 不在该数组中
if __name__ == "__main__":
    nums = [1, 6, 9, 10]
    target = 1
    re = binarySearch(nums, target)
    print(re)
    pass
