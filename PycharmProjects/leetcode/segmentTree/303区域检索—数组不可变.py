class NumArray:
    def __init__(self, nums):
        self.num_array = nums
        self.len_nums = len(nums)
        self.segment_tree = [0 for _ in range(len(nums) * 4)]
        self.set_segment_tree(0, 0, self.len_nums - 1)

    def sumRange(self, i: int, j: int) -> int:
        return self.sum_range(0, 0, self.len_nums-1, i, j)

    def sum_range(self, index, l, r, i, j):
        if l == i and r == j:
            return self.segment_tree[index]

        mid = l + (r - l)//2
        if i > mid:
            return self.sum_range(index*2+2, mid+1, r, i, j)
        elif j <= mid:
            return self.sum_range(index * 2 + 1, l, mid, i, j)
        else:
            return self.sum_range(index*2 + 1, l, mid, i, mid) + \
                   self.sum_range(index*2 + 2, mid+1, r, mid+1, j)


    # 表示index位置，sum[l,r]
    def set_segment_tree(self, index, l, r):
        if r == -1:
            return
        if l == r:
            self.segment_tree[index] = self.num_array[l]
            return self.num_array[l]

        mid = l + (r-l)//2
        self.segment_tree[index] = self.set_segment_tree(2*index+1, l, mid)\
                                   + self.set_segment_tree(2*index+2, mid+1, r)

        return self.segment_tree[index]


if __name__ == "__main__":
    nums = []
    so = NumArray(nums)


