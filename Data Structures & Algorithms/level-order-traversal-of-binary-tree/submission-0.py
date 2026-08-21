# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: list[list[int]] = []
        node_list = deque()
        node_list.append(root)
        while node_list:
            curr_level = []
            for i in range(len(node_list)):
                curr_node = node_list.popleft()
                if curr_node:
                    curr_level.append(curr_node.val)
                    node_list.append(curr_node.left)
                    node_list.append(curr_node.right)

            if curr_level:
                res.append(curr_level)

        return res