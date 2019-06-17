
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res_set = set()
        for word in words:
            res = ''
            for letter in word:
                res += l[ord(letter) - ord('a')]

            res_set.add(res)
        return len(res_set)

words = ["gin", "zen", "gig", "msg"]

if __name__ == '__main__':
    so = Solution()
    print(so.uniqueMorseRepresentations(words))