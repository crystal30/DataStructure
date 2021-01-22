# 暴力破解，超时
from copy import copy, deepcopy
class Solution:
    def corpFlightBookings(self, bookings, n):
        if n == 0:
            return []
        bookings_list = [0 for _ in range(n)]
        for sub_bookings in bookings:
            j = sub_bookings[0]
            k = sub_bookings[1]
            num = sub_bookings[2]
            for i in range(j-1, k):
                bookings_list[i] += num

        return bookings_list

# 使用线段树,仍然超时
class Solution1:
    def __init__(self):
        self.segment_tree = None
        self.lazy_array = None
    def corpFlightBookings(self, bookings, n):
        self.segment_tree = [[] for _ in range(4*n)]
        self._set_segment_tree(0, 0, n-1)
        self.lazy_tree = deepcopy(self.segment_tree)
        for book in bookings:
            self._update(0, 0, n-1, book[0]-1, book[1]-1, book[2])

        return self.segment_tree[0]

    # 在数组[i,j]中的元素加num
    def _update(self, index, l, r, i, j, num):
        mid = l + (r - l) // 2
        if max(self.lazy_tree[index]) != 0:
            self.segment_tree[index] = copy(self.lazy_tree[index])
            if len(self.segment_tree[index]) != 1:
                self.lazy_tree[index * 2 + 1] = self.segment_tree[index][0:mid + 1 - l]
                self.lazy_tree[index * 2 + 2] = self.segment_tree[index][mid + 1 - l:]
            self.lazy_tree[index] = [0 for _ in range(len(self.lazy_tree))]

        if l == i and r == j:
            self.segment_tree[index] = [e + num for e in self.segment_tree[index]]
            if r - l != 0:
                self.lazy_tree[index*2+1] = self.segment_tree[index][0:mid+1-l]
                self.lazy_tree[index*2+2] = self.segment_tree[index][mid+1-l:]
            return self.segment_tree[index]


        if i > mid:
            right_child = self._update(index*2+2, mid+1, r, i, j, num)
            self.segment_tree[index][mid+1-l: r+1-l] = right_child
        elif j <= mid:
            left_child = self._update(index*2+1, l, mid, i, j, num)
            self.segment_tree[index][: mid+1-l] = left_child

        else:
            left_child = self._update(index*2+1, l, mid, i, mid, num)
            right_child = self._update(index*2+2, mid+1, r, mid+1, j, num)
            self.segment_tree[index][:mid+1-l] = left_child
            self.segment_tree[index][mid+1-l:r+1-l] = right_child
        return self.segment_tree[index]

    def _set_segment_tree(self, index, l, r):
        if l == r:
            self.segment_tree[index] = [0]
            return [0]

        mid = l + (r - l)//2
        left_child = self._set_segment_tree(index*2+1, l, mid)
        right_child = self._set_segment_tree(index*2+2, mid+1, r)
        self.segment_tree[index] = copy(left_child)
        self.segment_tree[index].extend(right_child)
        return self.segment_tree[index]


# 神奇的脑回路
class Solution2:
    def corpFlightBookings(self, bookings, n):
        # counter i-1 表示第i站的变化
        counter = [0 for _ in range(n)]
        # 乘坐人数, 表示第i站的人数 flight_num[i] = flight_num[i-1] + counter[i]
        flight_num = [0 for _ in range(n)]
        for book in bookings:
            # 表示从第i站上车num人，从第j+1站下车num人
            i = book[0]
            j = book[1]
            num = book[2]
            counter[i-1] += num
            if j < n:
                counter[j] -= num

        flight_num[0] = counter[0]
        for i in range(1, n):
            flight_num[i] = flight_num[i-1] + counter[i]

        return flight_num





if __name__ == "__main__":
    so = Solution2()
    # bookings = [[1,2,10],[2,3,20],[2,5,25]]
    # n = 5
    bookings = [[1, 2, 20], [1, 4, 15], [2, 4, 35], [2, 3, 50], [1, 1, 15]]
    n = 5
    re = so.corpFlightBookings(bookings, n)
    print(re)