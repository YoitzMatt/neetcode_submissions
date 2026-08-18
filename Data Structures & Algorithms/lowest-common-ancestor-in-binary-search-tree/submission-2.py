# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        nodes = deque()
        nodes.append(root)

        while nodes:
            curr = nodes.pop()
            if p.val > curr.val and q.val > curr.val:
                nodes.append(curr.right)
            elif p.val < curr.val and q.val < curr.val:
                nodes.append(curr.left)
            else:
                return curr
                