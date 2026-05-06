# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        ans=[]
        tmp=root
        
        while stack or tmp:
            if tmp:
                stack.append(tmp)
                tmp=tmp.left
            else:
                top=stack.pop()
                ans.append(top.val)
                if top:
                    tmp=top.right

                    
        
        return ans

        stack=[]
        tmp=root
        ans=[]
        
        while stack or tmp:
            while tmp:
                stack.append(tmp)
                tmp=tmp.left
            tmp=stack.pop()
            ans.append(tmp.val)
            
            tmp=tmp.right
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        if root==None:
            return []
        ans=[]
        if root:
    
            ans=self.inorderTraversal(root.left)
            ans=ans+[root.val]
            right=self.inorderTraversal(root.right)
            ans=ans+right
            
        return ans
