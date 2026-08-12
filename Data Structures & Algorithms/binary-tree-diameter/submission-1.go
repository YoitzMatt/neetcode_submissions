/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func diameterOfBinaryTree(root *TreeNode) int {
    res := 0

    var dfs func(*TreeNode) int
    dfs = func (curr *TreeNode) int {
        if curr == nil {
            return 0
        }

        res = max(res, dfs(curr.Left) + dfs(curr.Right))
        return 1 + max(dfs(curr.Left), dfs(curr.Right))
    }

    dfs(root)
    return res
}
