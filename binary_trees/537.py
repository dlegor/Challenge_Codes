# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root==None:
            return False
        else:
            
            targetSum=targetSum-root.val
            
            if root.left==None and root.right==None and targetSum==0:
                return True
            
            if root.left==None and root.right==None and targetSum!=0:
                return False
        
        
            
        a=self.hasPathSum(root.left,targetSum)
        b=self.hasPathSum(root.right,targetSum)
            
        return True if(a==True or b==True) else False
