# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs approach - travel through every possible path and keep track of sum
        # if node value is greater than curr highest, then change curr highest for that path
        # and add to total sum

        self.res = 0

        def dfs(curr, currHigh):
            if not curr:
                return
            if curr.val >= currHigh:
                self.res += 1 
                currHigh = curr.val
            
            dfs(curr.left, currHigh)
            dfs(curr.right, currHigh)

        dfs(root, root.val)
        return self.res