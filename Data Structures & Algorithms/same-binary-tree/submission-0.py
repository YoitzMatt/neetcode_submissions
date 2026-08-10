# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        to_visit = [(p, q)]

        while to_visit:
            node1, node2 = to_visit.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            to_visit.append((node1.left, node2.left))
            to_visit.append((node1.right, node2.right))

        return True