# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque([root])
        res = []

        while queue:
            queueLen = len(queue)
            rightmost = None

            for i in range(queueLen):
                node = queue.popleft()
                if node:
                    rightmost = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightmost:
                res.append(rightmost.val)
        return res

        