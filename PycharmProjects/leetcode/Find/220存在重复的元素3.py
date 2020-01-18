class Solution:

    # 用时比较多
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        '''

        :param nums: List[int]
        :param k:
        :param t:
        :return:
        '''

        n = len(nums)
        record = list()
        for i in range(n):
            record.sort()
            if self.find_e(record, nums[i]-t, nums[i]+t):
                    return True

            record.append(nums[i])

            if len(record) == k+1:
                record.remove(nums[i-k])

        return False

    # 超出时间限制
    def containsNearbyAlmostDuplicate1(self, nums, k: int, t: int) -> bool:
        '''

        :param nums: List[int]
        :param k:
        :param t:
        :return:
        '''

        n = len(nums)
        record = list()
        for i in range(n):
            n = len(record)
            if n > 0:
                record.sort()
                if record[-1] < nums[i]-t or record[0] > nums[i]+ t:
                    record.append(nums[i])
                elif self.find_e(record, nums[i]-t, nums[i]+t):
                        return True
                else:
                    record.append(nums[i])
            else:
                record.append(nums[i])

            if len(record) == k+1:
                record.remove(nums[i-k])

        return False

    # 查找record 中是否存在[a,b]之间的数
    def find_e(self, record, a, b):
        # 查找record[l,r] 之间的元素是否在 [a,b]之间
        # record 是从小到大排好序的
        l = 0
        r = len(record) - 1

        while l <= r:
            mid = (r - l) // 2 + l
            if record[mid] > b:
                r = mid - 1

            elif record[mid] < a:
                l = mid + 1

            else: # record[mid] >= a and record[mid] <= b
                return True

        return False



if __name__ == "__main__":
    so = Solution()
    nums = [1,2]
    k = 0
    t = 1
    re = so.containsNearbyAlmostDuplicate1(nums, k, t)
    print(re)

