class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0]), -1, -1):
            prefix = strs[0][0:i]

            for s in strs:
                if s[0:i] != prefix:
                    break
            else :
                return prefix

        