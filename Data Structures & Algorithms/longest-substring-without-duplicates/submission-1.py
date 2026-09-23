class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        windowSet = set()

        l, r = 0, 0
        while r < len(s):
            while s[r] in windowSet: 
                windowSet.remove(s[l])
                l += 1

            windowSet.add(s[r])
            res = max(res, len(windowSet))
            r += 1
        return res
        