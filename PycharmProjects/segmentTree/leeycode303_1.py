class NumArray(object):

    def __init__(self, a):
        self._n = len(a)
        self._tree = [0] * 4 * self._n
        self._build_tree(a, 0, self._n - 1, 0)

    def _build_tree(self, a, lo, hi, w):
        if lo == hi:
            self._tree[w] = a[lo]
        elif lo < hi:
            mid = lo + (hi - lo) // 2
            self._build_tree(a, lo, mid, 2 * w + 1)
            self._build_tree(a, mid + 1, hi, 2 * w + 2)
            self._tree[w] = self._tree[2 * w + 1] + self._tree[2 * w + 2]


    def sumRange(self, i, j):
        return self._sum_range(i, j, 0, self._n - 1, 0)

    def _sum_range(self, q_lo, q_hi, lo, hi, w):
        if q_lo <= lo and hi <= q_hi:
            return self._tree[w]
        if q_lo > hi or q_hi < lo:
            return 0
        mid = lo + (hi - lo) // 2
        return self._sum_range(q_lo, q_hi, lo, mid, 2 * w + 1) + self._sum_range(q_lo, q_hi, mid + 1, hi, 2 * w + 2)


