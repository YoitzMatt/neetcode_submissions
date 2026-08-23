# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(curr, biggest):
            if not curr:
                return
            
            nonlocal res
            if curr.val >= biggest:
                res += 1
                
            dfs(curr.left, max(biggest, curr.val))
            dfs(curr.right, max(biggest, curr.val))

        dfs(root, root.val)
        return res