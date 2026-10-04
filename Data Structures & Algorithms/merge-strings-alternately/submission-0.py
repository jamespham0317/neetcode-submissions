class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        i1, i2 = 0, 0

        while i1 < len(word1) and i2 < len(word2):
            res += word1[i1] + word2[i2]
            i1 += 1
            i2 += 1

        res += word1[i1:]
        res += word2[i2:]

        return res