class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def isPalindrom(s):
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l + 1: r + 1], s[l:r]
                return isPalindrom(skipL) or isPalindrom(skipR)

            l += 1
            r -= 1

        return True
