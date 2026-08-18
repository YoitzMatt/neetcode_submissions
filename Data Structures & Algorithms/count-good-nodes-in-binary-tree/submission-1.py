# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res: int = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)
        return self.res
                    
    def dfs(self, curr: TreeNode, biggest_seen: int):
        if not curr:
            return
                
        if curr.val >= biggest_seen:
            self.res += 1
            self.dfs(curr.right, curr.val)
            self.dfs(curr.left, curr.val)
        else:
            self.dfs(curr.right, biggest_seen)
            self.dfs(curr.left, biggest_seen)