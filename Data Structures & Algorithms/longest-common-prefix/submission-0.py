class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(201):
            prefix = strs[0][0:i]

            for s in strs:
                if len(s) < i or s[0:i] != prefix:
                    return s[0:i - 1]


        