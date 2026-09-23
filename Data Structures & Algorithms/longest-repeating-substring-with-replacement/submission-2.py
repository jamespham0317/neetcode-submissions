class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        charset = set(s)

        for c in charset:
            kLeft = k
            l = 0
            for r in range(len(s)):
                if s[r] != c: 
                    kLeft -= 1

                while kLeft < 0:
                    if s[l] != c: 
                        kLeft += 1
                    l += 1
                maxLen = max(maxLen, r - l + 1)
        return maxLen
        