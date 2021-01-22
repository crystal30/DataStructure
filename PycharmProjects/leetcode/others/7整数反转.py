class Solution:
    def reverse(self, x: int):
        str_x = str(x)
        len_x = len(str_x)
        if str_x[0] == "-":
            reverse_x = int("-" + str_x[::-1][:len_x - 1])
        else:
            reverse_x = int(str_x[::-1])

        if reverse_x > 2147483647 or reverse_x < -2147483648:
            return 0
        else:
            return reverse_x


if __name__ == "__main__":
    so = Solution()
    x = 120
    re = so.reverse(x)
    print(re)