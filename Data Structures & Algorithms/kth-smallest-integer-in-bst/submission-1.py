# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(curr: TreeNode):
            if not curr:
                return

            nonlocal res
            res.append(curr.val)
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        res = sorted(res)
        return res[k-1]
            