# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # how to get THE smallest element? just go all the way left
        # second smallest element - parent node
        # third smallest element - right child node
        # idea: go left as far as possible, then traverse back up then to other child
        # each node in left subtree is less than the parent, so traverse everything before heading back up
        # inorder
        # count number of times traversing

        arr = []

        def dfs(curr): #use a dfs approach to traverse the tree
            if not curr:
                return
            
            dfs(curr.left) #go as far left as possible until it hits base case
            arr.append(curr.val) # add that value
            dfs(curr.right) #go right until base case which then pops back to parent

        dfs(root)
        return arr[k - 1] #kth element
            