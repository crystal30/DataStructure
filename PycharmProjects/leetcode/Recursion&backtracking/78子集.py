class Solution:

    def subsets(self, nums):
        len_nums = len(nums)
        res = [[], [nums[0]]]

        for i in range(1, len_nums):
            sub_res = []
            for e in res:
                temp_e = e.copy()
                temp_e.append(nums[i])
                sub_res.append(temp_e.copy())
            res.extend(sub_res)
        return res

if __name__ == "__main__":
    so = Solution()
    nums = [1,2,3,4]
    re = so.subsets(nums)
    print(re)