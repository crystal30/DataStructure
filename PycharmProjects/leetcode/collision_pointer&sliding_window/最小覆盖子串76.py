#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter,defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = Counter(t)
        s_dict = defaultdict(int)

        s_len = len(s)
        t_len = len(t)

        res = ''
        start = 0

        for i in range(s_len):
            e = s[i]
            if i < t_len: # 需要看一下，是否i=3时，不进入
                s_dict[e] += 1
                continue

            while self.is_contains(s_dict, t_dict):
                next_res_len = i - start
                if res == '' or len(res) > next_res_len:
                    res = s[start:i]

                start_e = s[start]
                s_dict[start_e] -= 1
                start += 1

            s_dict[e] += 1

        if self.is_contains(s_dict, t_dict):
            next_res_len = s_len - start
            if res == '' or len(res) > next_res_len:
                res = s[start:s_len]

        while self.keys_contains(s_dict, t_dict) and start < s_len:
            start_e = s[start]
            s_dict[start_e] -= 1
            start += 1

            if self.is_contains(s_dict, t_dict):
                next_res_len = s_len - start
                if len(res) > next_res_len:
                    res = s[start:s_len]

        return res

    def keys_contains(self, s_dict, t_dict):
        t_dict_keys = set(t_dict.keys())
        s_dict_keys = set(s_dict.keys())

        if(len(t_dict_keys.difference(s_dict_keys)) == 0):
            return True
        else:
            return False

    def is_contains(self, s_dict, t_dict):

        t_dict_keys = set(t_dict.keys())
        s_dict_keys = set(s_dict.keys())

        if len(t_dict_keys.difference(s_dict_keys)) == 0:
            for k in t_dict_keys:
                if t_dict[k] > s_dict[k]:
                    return False
            return True

        else:
            return False



if __name__ == "__main__":
    S = "abc"
    T = "b"
    so = Solution()
    print(so.minWindow(S, T))
