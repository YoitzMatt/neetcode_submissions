# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(curr):
            nonlocal res

            if not curr:
                return 0

            res = max(res, dfs(curr.right) + dfs(curr.left))
            return 1 + max(dfs(curr.right), dfs(curr.left))

        dfs(root)
        return res