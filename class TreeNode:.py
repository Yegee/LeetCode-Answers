class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
root = [1,2,3,null,null,4]