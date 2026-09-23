class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        neighbours = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                neighbours[pattern].append(word)

        queue = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighbour in neighbours[pattern]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
            res += 1
        return 0