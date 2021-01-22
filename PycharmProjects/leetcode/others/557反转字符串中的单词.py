class Solution:
    def reverseWords(self, s: str):
        s_list = s.split(" ")
        s_list = [e[::-1] for e in s_list]
        return " ".join(s_list)

if __name__ == "__main__":
    so = Solution()
    s = "Let's"
    re = so.reverseWords(s)
    print(re)
