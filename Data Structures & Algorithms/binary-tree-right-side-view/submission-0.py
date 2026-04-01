# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #O(n) time we are traversing every node once
        # we will use a bfs and get the last element in the level at each level
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            q_len = len(q)
            levels = []
            for i in range(q_len):
                curr = q.popleft()
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
                    levels.append(curr.val)
            if levels:
                res.append(levels[len(levels) - 1])
        return res