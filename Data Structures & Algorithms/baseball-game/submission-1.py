class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []

        for o in operations:
            if o == '+':
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif o == 'D':
                res += stack[-1] * 2
                stack.append(stack[-1] * 2)
            elif o == 'C':
                res -= stack.pop()
            else:
                res += int(o)
                stack.append(int(o))

        return res
            