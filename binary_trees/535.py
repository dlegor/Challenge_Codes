# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Solution bottom-down
        
        if root==None:
            return 0
        
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        
        return max(r,l)+1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Solution top-down
        
        ans=0
        depth=0
        if root==None:
            return 0
        
        if root.left==None and root.right==None:    
            ans=max(ans,depth)
            
        depth+=1
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        ans=max(depth+l,depth+r)
        return ans
True