class Solution:
    def decodeString(self, s: str):
        stack = []
        for sub_s in s:
            # 因为输入的字符串总是有效的，所以当sub_s == "]"时，不用判断stack是否为空
            if sub_s == "]":
                encode_s = ""
                while stack[-1] != "[":
                    encode_s = stack.pop() + encode_s

                stack.pop()
                num = ""
                while stack[-1] in "1234567890":
                    num = stack.pop() + num
                    if len(stack) == 0:
                        break

                stack.append(encode_s * int(num))
            else:
                stack.append(sub_s)

        return "".join(stack)


if __name__ == "__main__":
    so = Solution()
    s = "3[a2[c]]"
    re = so.decodeString(s)
    print(re)


