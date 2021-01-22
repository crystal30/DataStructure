# 只有一半的用例会通过
# 不通过的原因可能是：此做法只是判断了左边和右边，而有可能后边的改变了，前面的也可能跟着改变
class Solution:
    def __init__(self):
        self.candy_list = None
        self.len_ratings = None


    def candy(self, ratings):
        self.len_ratings = len(ratings)
        if self.len_ratings == 0:
            return 0
        if self.len_ratings == 1:
            return 1

        self.candy_list = [1 for _ in range(self.len_ratings)]
        for i, rating in enumerate(ratings):
            # 检查ratings[i],如果其评级小于邻居评级，返回-1；若评级大于邻居评级，返回大于邻居的评级的最大的糖果数
            candy_num = self.check_rating(i, rating, ratings)
            if candy_num == -1:
                continue
            else:
                self.candy_list[i] = candy_num + 1

        return sum(self.candy_list)


    def check_rating(self, index, rating, ratings):
        candy_num = -1
        # 如果有左邻居，且左邻居的评级小于当前评级，且糖果个数>=当前评级的小朋友
        if index - 1 >= 0 and \
                rating > ratings[index - 1] and \
                self.candy_list[index] <= self.candy_list[index-1]:
            candy_num = max(self.candy_list[index-1], candy_num)

        # 查看右邻居
        if index + 1 < self.len_ratings and \
                rating > ratings[index + 1] and \
                self.candy_list[index] <= self.candy_list[index + 1]:
            candy_num = max(self.candy_list[index + 1], candy_num)

        return candy_num



# 这个超时，会通过44个用例
class Solution1:
    def candy(self, ratings):
        len_ratings = len(ratings)
        if len_ratings == 0:
            return 0
        if len_ratings == 1:
            return 1

        candy_list = [1 for _ in range(len_ratings)]
        flag =  True
        while flag:
            flag = False
            for i, rating in enumerate(ratings):
                if i - 1 >= 0 and \
                        rating > ratings[i - 1] and \
                        candy_list[i] <= candy_list[i - 1]:

                    candy_list[i] = candy_list[i - 1] + 1
                    flag = True

                # 查看右邻居
                if i + 1 < len_ratings and \
                        rating > ratings[i + 1] and \
                        candy_list[i] <= candy_list[i + 1]:

                    candy_list[i] = candy_list[i + 1] + 1
                    flag = True

        return sum(candy_list)


class Solution2:
    def candy(self, ratings):
        len_ratings = len(ratings)
        if len_ratings == 0:
            return 0
        if len_ratings == 1:
            return 1

        left_to_right_candy = [1 for _ in range(len_ratings)]
        right_to_left_candy = [1 for _ in range(len_ratings)]
        for i, rating in enumerate(ratings):
            # 左邻居
            if i - 1 >= 0 and \
                    rating > ratings[i - 1] and \
                    left_to_right_candy[i] <= left_to_right_candy[i - 1]:

                left_to_right_candy[i] = left_to_right_candy[i - 1] + 1

            # 查看右邻居
            if i + 1 < len_ratings and \
                    rating > ratings[i + 1] and \
                    left_to_right_candy[i] <= left_to_right_candy[i + 1]:

                left_to_right_candy[i] = left_to_right_candy[i + 1] + 1

        for i in range(len_ratings-1, -1, -1):
            # 左邻居
            if i - 1 >= 0 and \
                    ratings[i] > ratings[i - 1] and \
                    right_to_left_candy[i] <= right_to_left_candy[i - 1]:

                right_to_left_candy[i] = right_to_left_candy[i - 1] + 1

            # 查看右邻居
            if i + 1 < len_ratings and \
                    ratings[i] > ratings[i + 1] and \
                    right_to_left_candy[i] <= right_to_left_candy[i + 1]:

                right_to_left_candy[i] = right_to_left_candy[i + 1] + 1

        candy_list = [max(left_to_right_candy[i],right_to_left_candy[i]) for i in range(len_ratings)]
        return sum(candy_list)

if __name__ == "__main__":
    so = Solution2()
    ratings = [1,0,2]
    re = so.candy(ratings)
    print(re)

