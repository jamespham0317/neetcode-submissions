class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time: 
            return ''

        targetArray = self.time[key]
        if targetArray[0][0] > timestamp:
            return ''

        l, r = 0, len(targetArray) - 1

        while l < r:
            m = - (( - (r - l)) // 2) + l

            if targetArray[m][0] > timestamp:
                r = m - 1
            else:
                l = m
        return targetArray[l][1]
