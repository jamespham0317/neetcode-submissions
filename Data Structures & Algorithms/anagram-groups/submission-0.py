class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            letterCount = [0] * 26
            for c in s:
                letterCount[ord(c) - ord("a")] += 1
            map[tuple(letterCount)].append(s)
        return list(map.values())

        