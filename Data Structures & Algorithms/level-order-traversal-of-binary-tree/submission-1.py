# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = collections.deque()
        if root: queue.append(root) 

        while queue:
            subList = []
            for i in range(len(queue)):
                node = queue.popleft()
                subList.append(node.val)
                if node.left: queue.append(node.left) 
                if node.right: queue.append(node.right) 
            if subList: res.append(subList)
        return res


