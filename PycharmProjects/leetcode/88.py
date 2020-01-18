class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2
        elif m>0 and n>0:
            if nums2[0] >= nums1[m-1]:
                nums1[-n:] = nums2
            elif nums1[0] >= nums2[n-1]:
                nums1[-m:] = nums1[:m]
                nums1[:n] = nums2
            else:
                i = 0
                j = 0
                while i < m+n and j <n:
                    if nums1[i] > nums2[j]:
                        nums1.insert(i, nums2[j])
                        nums1.pop()
                        j += 1
                    i += 1
                if j < n:
                    nums1[j-n:] = nums2[j:]

    def merge1(self, nums1, m: int, nums2, n: int) -> None:
            """
            Do not return anything, modify nums1 in-place instead.
            """

            if m == 0:
                nums1[:] = nums2[:]

            elif m >= 1 and n >= 1:
                if nums1[0] >= nums2[n - 1]:
                    nums1[-m:] = nums1[:m]
                    nums1[:n] = nums2[:]  # 找一组数测一下
                elif nums2[0] >= nums1[m - 1]:
                    nums1[-n:] = nums2[:]
                else:
                    i = 0
                    j = 0
                    temp = []
                    while i < m and j < n:
                        if nums1[i] > nums2[j]:
                            temp.append(nums2[j])
                            j += 1
                        else:
                            temp.append(nums1[i])
                            i += 1

                    if i < m:
                        temp.extend(nums1[i:m])
                    elif j < n:
                        temp.extend(nums2[j:n])

                    nums1[:] = temp[:]

if __name__ == "__main__":
    nums1 = [0, 0, 3, 0, 0, 0, 0, 0, 0]
    m = 3
    nums2 = [-1, 1, 1, 1, 2, 3]
    n = 6
    so = Solution()
    so.merge(nums1, m, nums2, n)
    pass

