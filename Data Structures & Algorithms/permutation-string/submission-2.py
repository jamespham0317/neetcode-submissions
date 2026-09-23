class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = sorted(s1)
        for i in range(len(s2) - len(s1) + 1):
            curr = sorted(s2[i:i + len(s1)])

            if need == curr: return True

        return False



        