from collections import Counter
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        k = 0 # nums[0,k) 为排序正确的数组
        for i in range(len_nums):
            if nums[k] == 2:
                nums.append(nums.pop(k))
            elif nums[k] == 0:
                nums.insert(0, nums.pop(k))
                k += 1
            else:
                k += 1

    def sortColors1(self, nums):
        nums_count = Counter(nums)
        count_0 = nums_count.setdefault(0, 0)
        count_1 = nums_count.setdefault(1, 0)
        count_2 = nums_count.setdefault(2, 0)

        for j in range(count_0):
                nums[j] = 0
        for j in range(count_0, count_0 + count_1):
                nums[j] = 1
        for k in range(count_0 + count_1, count_0 + count_1 + count_2):
                nums[k] = 2

    def sortColors2(self, nums):

        # 统计 nums 中元素的个数
        nums_count = [0]*3
        for e in nums:
            assert e >= 0 and e <= 2
            nums_count[e] += 1

        index = 0
        for i in range(nums_count[0]):
            nums[index] = 0
            index += 1
        for j in range(nums_count[1]):
            nums[index] = 1
            index += 1
        for k in range(nums_count[2]):
            nums[index] = 2
            index += 1

    # 三路快排
    def sortColors3(self, nums):

        len_nums = len(nums)
        lt = 0 # nums[0, lt）中存放 < target的元素
        gt = len_nums # nums[gt, len_nums-1] 存放 >target的元素；[lt, gt)存放==target的元素
        i = 0

        while i<gt and lt < gt:
            if nums[i] == 1:
                i += 1
            elif nums[i] > 1:
                nums[i], nums[gt-1] = nums[gt-1], nums[i]
                gt -= 1
            else:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt += 1
                i += 1

    def sortColors4(self, nums):

        n = len(nums)
        if n > 1:
            lt = -1 # nums[0,lt]<1, nums(lt,gt)==1, nums[gt:]>1
            gt = n
            i = 0
            while i < gt and lt < gt:
                if nums[i] == 1:
                    i += 1

                elif nums[i] < 1:
                    lt += 1
                    nums[lt], nums[i] = nums[i], nums[lt]
                    i += 1

                else:
                    gt -= 1
                    nums[i], nums[gt] = nums[gt], nums[i]

    # 下边这个感觉最good
    def sortColors5(self, nums):
        n = len(nums)  # nums[0, lt] < 1; nums(lt, gt) == 1; nums[gt:] > 1
        if n > 1:
            gt = n
            lt = -1
            i = 0
            while i < gt:
                if nums[i] == 1:
                    i += 1
                elif nums[i] > 1:
                    gt -= 1
                    nums[i], nums[gt] = nums[gt], nums[i]
                else:
                    lt += 1
                    nums[i], nums[lt] = nums[lt], nums[i]
                    i += 1


if __name__ == "__main__":
    nums = [0]
    so = Solution()
    so.sortColors3(nums)
    pass

