# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # since we are looking for ONE path not all paths, use DFS
        # DFS recursive, add up


        
        def dfs(node, currSum):
            if not node:
                return False
            
            currSum += node.val
            if not node.right and not node.left:
                return currSum == targetSum
            
            return dfs(node.right, currSum) or dfs(node.left, currSum)            
        
        return dfs(root, 0)
