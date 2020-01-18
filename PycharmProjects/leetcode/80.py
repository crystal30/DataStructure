class Solution:
    def removeDuplicates(self, nums):
        # 是排好顺序的数组
        len_nums = len(nums)
        if len_nums == 0:
            return 0

        e = nums[0]  # 为要处理的元素
        count = 1  # 重复元素的个数
        k = 1  # nums[0,k) 为要保留的数组
        for _ in range(1, len_nums):
            if nums[k] == e:
                if count < 2:
                    count += 1
                    k += 1
                else:
                    nums.pop(k)
            else:
                e = nums[k]
                count = 1
                k += 1
        return k

if __name__ == "__main__":
    nums = [0,0,1,1,1,1,2,3,3]
    so = Solution()
    re = so.removeDuplicates(nums)
    print(re)
    pass

