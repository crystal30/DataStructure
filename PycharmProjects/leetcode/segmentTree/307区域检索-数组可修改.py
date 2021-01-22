class NumArray:
    def __init__(self, nums):
        self.num_array = nums
        self.len_nums = len(nums)
        self.segment_tree = [0 for _ in range(len(nums) * 4)]
        self.set_segment_tree(0, 0, self.len_nums - 1)

    def sumRange(self, i: int, j: int) -> int:
        return self.sum_range(0, 0, self.len_nums-1, i, j)

    def update(self, i: int, val: int):
        self._update(0, 0, self.len_nums-1, i, val)

    def _update(self, index, l, r, i, val):
        if l == r == i:
            self.segment_tree[index] = val
            return val

        mid = l + (r-l)//2
        if i > mid:
            self.segment_tree[index] = self.segment_tree[index*2+1] + self._update(index*2+2, mid+1, r, i, val)
        else: #  i <= mid:
            self.segment_tree[index] = self._update(index*2+1, l, mid, i, val) + self.segment_tree[index*2+2]

        return self.segment_tree[index]


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
    # re = so.sumRange(0,2)
    # print(re)
    # so.update(1,2)
    # print(so.sumRange(0, 2))



