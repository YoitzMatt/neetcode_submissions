# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
            res = 0
            def dfs(curr: TreeNode, biggest_seen: int):
                if not curr:
                    return
                
                nonlocal res
                if curr.val >= biggest_seen:
                    res += 1
                    dfs(curr.right, curr.val)
                    dfs(curr.left, curr.val)
                else:
                    dfs(curr.right, biggest_seen)
                    dfs(curr.left, biggest_seen)

            dfs(root, root.val)
            return res
                    