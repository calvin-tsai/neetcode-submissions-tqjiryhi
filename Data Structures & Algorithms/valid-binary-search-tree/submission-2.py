# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we can use a dfs approach for every node
        # traverse every node, if there are any invalid child nodes return false
        # basically if left and right are true return true
        # if any node is false the whole thing will be false
        # otherwise return true
        # follow up question can the nodes be equal?
        
        def dfs(curr, left, right):
            if not curr:
                return True # means we got all the way to the bottom without returning
            if not (left < curr.val < right):
                return False
            return dfs(curr.right, curr.val, right) and dfs(curr.left, left, curr.val)
        return dfs(root, float('-inf'), float('inf'))
