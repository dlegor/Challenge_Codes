# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left,root.right)
    
    def isMirror(self,root1: Optional[TreeNode],root2: Optional[TreeNode])->bool:
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        
        if root1.val==root2.val:
            if self.isMirror(root1.left,root2.right):
                if self.isMirror(root1.right,root2.left):
                    return True
            else:
                return False
    
        return False
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #iterative
        if root==None:
            return True
        
        if root.right==None and root.left==None:
            return True
    
        stack=[]
        stack.append((root.left,root.right))
        while stack:
        
            node_l,node_r=stack.pop()

            if node_l==None and node_r==None:
                continue
                
            if (node_l and  not node_r) or ( not node_l and node_r):
                return False
            
            if node_l and node_r and node_l.val!=node_r.val:
                return False
            
            stack.append((node_l.left,node_r.right))
            stack.append((node_l.right,node_r.left))
            
        return True
    