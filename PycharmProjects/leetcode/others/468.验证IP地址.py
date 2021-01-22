class Solution:
    def validIPAddress(self, IP: str):
        if self.is_ipv4(IP):
            return "IPv4"
        elif self.is_ipv6(IP):
            return "IPv6"
        else:
            return "Neither"

    def is_ipv4(self, IP):
        ip_list = IP.split(".")
        if len(ip_list) != 4:
            return False
        for e in ip_list:
            if len(e) == 0:
                return False
            for bit_e in e:
                if bit_e not in "0123456789":
                    return False
            len_e = len(e)
            int_e = int(e)
            if int_e < 0 or int_e > 255:
                return False
            elif len_e >= 2 and e[0] == "0":
                return False

        return True

    def is_ipv6(self, IP):
        ip_list = IP.split(":")
        if len(ip_list) != 8:
            return False

        for e in ip_list:
            #需要控制在16bit内
            if len(e) > 4 or len(e) == 0:
                return False
            for bit_e in e:
                if bit_e not in "0123456789abcdefABCDEF":
                    return False
        return True

if __name__ == "__main__":
    so = Solution()
    IP = "2001:0db8:85a3:00000:0:8A2E:0370:7334"
    re = so.validIPAddress(IP)
    print(re)


