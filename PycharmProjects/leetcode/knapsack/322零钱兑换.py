
# 这个超时
class Solution:
    def __init__(self):
        self.memo = None
        self.min_coin = 0
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        self.min_coin = min(coins)
        if self.min_coin > amount:
            return -1

        self.memo = [100000 for _ in range(amount+1)]
        self.memo[0] = 0
        self.coin_change(coins, amount)

        if self.memo[amount] >= 100000:
            return -1
        else:
            return self.memo[amount]

    def coin_change(self, coins, amount):
        if amount == 0:
            self.memo[amount] = 0
            return 0
        if self.min_coin > amount:
            self.memo[amount] += 1
            return self.memo[amount]

        if self.memo[amount] != 100000:
            return self.memo[amount]

        count = [self.coin_change(coins, amount-coin) for coin in coins if coin <= amount]
        self.memo[amount] = 1 + min(count)
        return self.memo[amount]

# 用动态规划的思路
class Solution1:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        min_coin = min(coins)
        if min_coin > amount:
            return -1
        memo = [100000 for _ in range(amount+1)]
        memo[0] = 0

        for i in range(1, amount+1):
            if min_coin > i:
                continue
            memo[i] = 1 + min([memo[i - coin] for coin in coins if coin <= i])

        if memo[amount] >= 100000:
            return -1
        else:
            return memo[amount]


if __name__ == "__main__":
    so = Solution1()
    coins = [1]
    amount = 2
    re = so.coinChange(coins, amount)
    print(re)