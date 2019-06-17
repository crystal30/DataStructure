import collections
class Solution(object):
    #时间复杂度：O(N*KlogK) K为最长的字符串的长度，假设sorted(s)的时间复杂度为O(KlogK)
    #空间复杂度：O(N*K）
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

    #不调用 collections包
    # 时间复杂度：O(N*KlogK) K为最长的字符串的长度，假设sorted(s)的时间复杂度为O(KlogK)
    # 空间复杂度：O(N*K）
    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = dict()
        for s in strs:
            k = tuple(sorted(s))
            ans.setdefault(k, [])
            #如果key在字典中，则返回其值。如果没有，
            # 则插入值为default的key，并返回default。default默认为None
            ans[k].append(s)
        # return ans.values()  #dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
        return list(ans.values()) #good [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

if __name__ == "__main__":

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    so = Solution()
    re = so.groupAnagrams1(strs)
    print(re)
    pass