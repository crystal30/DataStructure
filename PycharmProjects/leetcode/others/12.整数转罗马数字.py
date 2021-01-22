class Solution:
    def intToRoman(self, num: int):
        num_dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M",
                    4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}

        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        re = ""
        while i < len(num_list):
            if num < num_list[i]:
                i += 1
            else:
                sub_num = num_list[i]
                re += num_dict[sub_num]
                num -= sub_num
            if num == 0:
                break

        return re

if __name__ == '__main__':
    so = Solution()
    re = so.intToRoman(8)
    print(re)