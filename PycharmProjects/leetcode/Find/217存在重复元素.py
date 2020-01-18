class Solution:
    def containsDuplicate(self, nums) -> bool:
        '''

        :param nums:  List[int]
        :return:
        '''

        n = len(nums)
        record = set()
        for i in range(n):
            if nums[i] in record:
                return True
            else:
                record.add(nums[i])

        return False


if __name__ == "__main__":
    so = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]
    re = so.containsDuplicate(nums)
    print(re)