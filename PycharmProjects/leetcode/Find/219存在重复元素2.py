class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        '''

        :param nums:  List[int]
        :param k:
        :return:
        '''
        n = len(nums)
        l = 0
        r = 1
        dd = dict()
        while r < n:
            if nums[l] not in dd:
                if nums[r] not in dd:
                    dd[nums[r]] = 1
                else:
                    dd[nums[r]] += 1
                r += 1
            else:
                return True

            if r - l > k+1:
                dd[nums[l+1]] -= 1
                if dd[nums[l+1]] == 0:
                    del dd[nums[l+1]]

                l += 1

        while l+1 < n:
            if nums[l] in dd:
                return True
            else:
                dd[nums[l + 1]] -= 1
                if dd[nums[l + 1]] == 0:
                    del dd[nums[l + 1]]

                l += 1

        return False

    def containsNearbyDuplicate1(self, nums, k: int) -> bool:
        '''

        :param nums: List[int]
        :param k:
        :return:
        '''

        record = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in record:
                return True
            else:
                record.add(nums[i])

            if len(record) == k+1:
                record.remove(nums[i-k])

        return False

if __name__ == "__main__":
    so = Solution()
    nums = [1,2,3,1,2,3]
    k = 2
    # nums = [1, 2, 3, 1]
    # k = 3
    # nums = [1, 0, 1, 1]
    # k = 1

    # nums = [1, 1, 1, 1]
    # k = 1

    re = so.containsNearbyDuplicate1(nums, k)
    print(re)