# 超出时间限制,最后一个用例不通过
class Solution:
    def countPrimes(self, n: int):
        if n <= 2:
            return 0
        if n <= 3:
            return 1
        if n <= 5:
            return 2
        if n <= 7:
            return 3
        if n <= 8:
            return 4
        memo = [0 for _ in range(n+1)]
        memo[0] = 0
        memo[1] = 0
        memo[2] = 0
        memo[3] = 1
        memo[4] = 2
        memo[5] = 2
        memo[6] = 3
        memo[7] = 3
        memo[8] = 4
        if n <= 8:
            return memo[n]

        for i in range(8, n):
            if self.is_prime(i):
                memo[i+1] = memo[i] + 1
            else:
                memo[i + 1] = memo[i]
        return memo[n]

    def is_prime(self, n):
        sqrt_i = int(n ** 0.5)
        for i in range(2, sqrt_i+1):
            if n % i == 0:
                return False
        return True

# 这种方法比较难理解
class Solution1:
    def countPrimes(self, n: int):
        if n <= 1:
            return 0
        if n == 2:
            return 1
        re = 0
        is_prime = [1 for _ in range(n)]
        for i in range(2, n):
            if is_prime[i] == 1:
                re += 1
                for j in range(i*i, n, i):
                    is_prime[j] = 0

        return re


if __name__ == '__main__':
    so = Solution1()
    n = 10
    re = so.countPrimes(n)
    print(re)

