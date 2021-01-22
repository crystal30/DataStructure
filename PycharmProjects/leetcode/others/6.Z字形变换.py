class Solution:
    def convert(self, s: str, numRows: int):
        len_s = len(s)
        if len_s <= numRows:
            return s
        # 行数为2时，是什么样子呢
        num_cols = (len_s // (numRows - 2 + numRows) + 1) * (numRows - 2 + 1)
        matrix_s = [["" for _ in range(num_cols)] for _ in range(numRows)]

        flag = 0
        i = 0
        j = 0
        for sub_s in s:
            matrix_s[i][j] = sub_s
            if flag == 0:
                i += 1
            else:
                i -= 1
                j += 1

            if i == numRows-1:
                flag = 1

            if i == 0:
                flag = 0

        re = ["".join(e) for e in matrix_s]
        return "".join(re)

if __name__ == "__main__":
    so = Solution()
    s = "LEETCODEISHIRING"
    numRows = 4
    re = so.convert(s, numRows)
    print(re)

