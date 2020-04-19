class Solution:
    def __init__(self):
        self.res = []
    def restoreIpAddresses(self, s: str):
        if s == '0000':
            return ['0.0.0.0']
        self._restore_ip(s, 0, [])
        return self.res

    def _restore_ip(self, s, i, sub_ip):
        if i == 4:
            if s == '':
                sub_ip_str = '.'.join(sub_ip)
                self.res.append(sub_ip_str)
            return

        for k in range(1, 4):
            if k > len(s):
                break

            if self.is_vaild_ip(s[:k]):
                sub_ip.append(s[:k])
                self._restore_ip(s[k:], i+1, sub_ip)
                sub_ip.pop()
            else:
                continue

        return

    def is_vaild_ip(self, s_ip):
        int_s = int(s_ip)

        if len(s_ip) > 1 and s_ip[0] == '0':
            return False

        if int_s > 255: # 修改一句话，时间相差24ms！！！ 比较：int_s >= 0 and int_s <= 255
            return False

        return True

if __name__ == "__main__":
    so = Solution()
    # s = "25525511135"
    # s = "0000"
    s = "0100"
    re = so.restoreIpAddresses(s)
    print(re)