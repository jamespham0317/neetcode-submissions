class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows - 1

        while l <= r:
            m = (r - l) // 2 + l

            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                targetArray = matrix[m]

                l1, r1 = 0, cols - 1
                while l1 <= r1:
                    m1 = (r1 - l1) // 2 + l1

                    if target < targetArray[m1]:
                        r1 = m1 - 1
                    elif target > targetArray[m1]:
                        l1 = m1 + 1
                    else:
                        return True

                break
        return False