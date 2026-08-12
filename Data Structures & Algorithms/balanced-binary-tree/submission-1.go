/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isBalanced(root *TreeNode) bool {
    res := true
    var dfs func(*TreeNode) int
    dfs = func(curr *TreeNode) int {
        if (curr == nil) {
            return 0
        }

        left := dfs(curr.Left)
        right := dfs(curr.Right)
        diff := right - left
        if (math.Abs(float64(diff)) > 1) {
            res = false
        }

        return 1 + max(left, right)
    }

    dfs(root)
    return res
}
