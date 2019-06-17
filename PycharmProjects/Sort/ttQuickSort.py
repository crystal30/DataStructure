class QuickSort:

    @classmethod
    def sort1(cls, nums):
        cls.__sort1(0, len(nums)-1, nums)
        return nums

    #对nums[l,r],前闭后闭的区间的元素进行排序
    @classmethod
    def __sort1(cls, l, r, nums):
        if l >= r:
            return
        #假设[l+1,....j]中存放的元素小于arr[l], [j+1,.....r]中的元素大于等于arr[l]
        j = l
        for i in range(l+1, r+1):
            if nums[i] < nums[l]:
                nums[j+1], nums[i] = nums[i], nums[j+1]
                j += 1
        nums[l], nums[j] = nums[j], nums[l]

        cls.__sort1(l, j-1, nums)
        cls.__sort1(j+1, r, nums)

    #双路快排
    #用上述方法，要不就是将小于和等于nums[l]的数放在一起；
    # 要么是将大于和等于nums[l]的数放在一起，即等于nums[l]的数都集中在一遍。
    #对于具有较多重复元素的数组来说，左右不平衡，递归时就不能构成比较一个平横的树(循环也是一样的)
    #所以，用双路快排的方法，将等于nums[l]的数随机的分配在左右两边。
    #假设nums[l+1,i)中存放元素<= nums[l], nums(ge,r]中存放的元素>=nums[l]
    @classmethod
    def sort2(cls, nums):
        cls.__Sort2(0,len(nums)-1,nums)
        return nums

    #对nums[l, r]范围内的元素进行排序
    @classmethod
    def __Sort2(cls, l, r, nums):
        if l >= r:
            return
        ge = r
        i = l+1
        while True:
            while i <= r and nums[i] <= nums[l]:
                i += 1
            while ge >= l+1 and nums[ge] >= nums[l]:
                ge -= 1
            if i>ge:
                break
            nums[i], nums[ge] = nums[ge], nums[i]
            i += 1
            ge -= 1
        nums[l], nums[ge] = nums[ge], nums[l]
        cls.__Sort2(l, ge-1, nums)
        cls.__Sort2(ge+1, r, nums)

    #双路快排算法中，虽然将重复的元素没有集中在一遍，保持了递归数的相对平衡，但是其对重复的元素进行了多遍的操作
    #改进3，3路快排
    #假设nums[l+1, lt]中元素<nums[l]; nums[lt+1, i-1]中元素=nums[l]; nums[gt,r]中元素>nums[l]
    @classmethod
    def sort3(cls, nums):
        cls.__Sort3(0, len(nums)-1, nums)
        return nums

    #对nums[l,r]前闭后闭区间中的元素进行排序
    @classmethod
    def __Sort3(cls, l, r, nums):
        if l >= r:
            return
        #改进
        # if r -l <= 15:
        #    #用插入排序
        #改进原因：1.元素数组比较小时，整个数组是近乎有序的概率比较大，插入排序对于有序的数组，时间复杂度为O(n)
        #2.即使按插入排序的时间复杂度是O(n2),其指令数为a*n2；快速排序的时间复杂度为O(nlogn),其指令数为b*O(nlogn)
        #而a<b,所以在n较小时 a*n2 < b*nlogn
        lt = l
        gt = r+1
        i = l+1
        while i<gt:
            if nums[i] < nums[l]:
                nums[lt+1], nums[i] = nums[i], nums[lt+1]
                lt += 1
                i += 1

            elif nums[i] > nums[l]:
                nums[gt-1], nums[i] = nums[i], nums[gt-1]
                gt -= 1
            else:
                i += 1
        nums[l], nums[lt] = nums[lt], nums[l]
        cls.__Sort3(l, lt-1, nums)
        cls.__Sort3(gt, r, nums)

    # 用列表生成式：
    # 时间复杂度O（nlogn）？通过实验，数据每增大一倍，运行速度就增大一倍（O(n)和O（nlogn）的大致符合这个规律）
    # 空间复杂度O(n)
    @classmethod
    def sort4(cls, nums):
        cls.__sort4(nums)
        return nums

    @classmethod
    def __sort4(cls, arr):
        if len(arr) <= 1:
            return arr
        v = nums[0]
        e = [x for x in arr if x == v] #e数组中存放与指定相等的元素
        l = [x for x in arr if x < v] #l数组中存放小于指定元素的元素
        g = [x for x in arr if x > v] #g数组中存放大于指定元素的元素
        cls.__sort4(l)
        cls.__sort4(g)
        arr[:] = l + e + g

    @classmethod
    def sort5(cls, alist):
        if len(alist) <= 1:
            return alist
        else:
            return cls.sort5([x for x in alist[1:] if x <= alist[0]]) + alist[0:1] + cls.sort5(
                [x for x in alist[1:] if x > alist[0]])












