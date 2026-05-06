# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        ans=[]
        if root:
            ans.append(root.val)
            left=self.preorderTraversal(root.left)
            right=self.preorderTraversal(root.right)
            ans+=left
            ans+=right
        
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iteratively
        if root==None:
            return []
        
        curr=root
        stack=[root]
        ans=[]
        while stack:
            cur=stack.pop()
            ans.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            
        
                
                
                
                
                
                    
            
        return ans
