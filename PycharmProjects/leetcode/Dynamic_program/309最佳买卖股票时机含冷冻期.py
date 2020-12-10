# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.len_prices = 0
        self.status_buy = None
        self.status_sell = None

    def maxProfit(self, prices):
        self.len_prices = len(prices)
        if self.len_prices <= 1:
            return 0

        if self.len_prices == 2:
            return max(0, prices[1]-prices[0])

        re_money = [-1 for _ in range(self.len_prices-1)]
        self.status_buy = [-1 for _ in range(self.len_prices)]
        self.status_sell = [-1 for _ in range(self.len_prices)]
        for i in range(self.len_prices - 1):
            re_money[i] = self._max_profit(prices, i, 1)

        return max(max(re_money),0)


    def _max_profit(self, prices, start_i, status):
        """

        :param price:
        :param status: 状态，1为买，2为卖
        :param p: 为目前的金钱数
        :return:
        """

        # 为买的状态
        if status == 1:
            if self.status_buy[start_i] != -1:
                return self.status_buy[start_i]

            if start_i == self.len_prices - 1:
                return 0

            max_p = []
            for i in range(start_i+1, self.len_prices):
                max_p.append(self._max_profit(prices, i, 2))

            start_i_buy_p = max(max(max_p), 0)
            self.status_buy[start_i] = -prices[start_i] + start_i_buy_p
            return -prices[start_i] + start_i_buy_p

        # 为卖的状态
        if status == 2:
            if self.status_sell[start_i] != -1:
                return self.status_sell[start_i]

            if start_i >= self.len_prices - 3:
                start_i_sell_p = prices[start_i]
                self.status_sell[start_i] = start_i_sell_p
                return start_i_sell_p

            max_p = []
            for i in range(start_i+2, self.len_prices):
                max_p.append(self._max_profit(prices, i, 1))

            start_i_sell_p = max(max(max_p), 0)
            self.status_sell[start_i] = prices[start_i] + start_i_sell_p
            return prices[start_i] + start_i_sell_p


class Solution1:
    def maxProfit(self, prices):
        len_prices = len(prices)
        if len_prices <= 1:
            return 0

        if len_prices == 2:
            return max(0, prices[1]-prices[0])

        buy_status = [-1 for _ in range(len_prices)]
        sell_status = [-1 for _ in range(len_prices)]

        buy_status[-1] = 0
        buy_status[-2] = max(0, prices[-1]-prices[-2])
        sell_status[-3:] = prices[-3:]

        index_list = [i for i in range(1, len_prices-2)]
        for i in index_list[::-1]:
            buy_status[i] = -prices[i] + max(sell_status[i+1:])
            sell_status[i-1] = prices[i-1] + max(buy_status[i+1:])

        buy_status[0] = -prices[0] + max(sell_status[1:])
        return max(buy_status)



if __name__ == "__main__":
    so = Solution1()
    prices = [6,1,3,2,4,7]
    re = so.maxProfit(prices)
    print(re)

