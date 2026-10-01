class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, r):
            m = (r - l) // 2 + l
            left = nums[l:m + 1]
            right = nums[m + 1:r + 1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] < right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1
            return arr


        def mergeSort(arr, l, r):
            if l == r:
                return arr

            m = (r - l) // 2 + l
            mergeSort(nums, l, m)
            mergeSort(nums, m + 1, r)
            merge(nums, l, r)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)