# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root==None:
            return []
        #queue and visited list
        q=[]
        visited=[]
        ans=[]
        #add the root
        q.append(root)
        visited.append(root)
        
        step=0
        
        while q:
            s=len(q)
            tmp=[]
            for i in range(s):
                
                cur=q.pop(0)
                
                if cur.left and (cur.left not in visited):
                    visited.append(cur.left)
                    q.append(cur.left)
                if cur.right and (cur.right not in visited):
                    visited.append(cur.right)
                    q.append(cur.right)
                 
                tmp.append(cur.val)
            print(tmp)
            ans.append(tmp)   
        return ans



#fater version
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root==None:
            return []
        #queue and visited list
        q=[]
        #visited=[]
        ans=[]
        #add the root
        q.append(root)
        #visited.append(root)
        
        
        while q:
            s=len(q)
            tmp=[]
            for i in range(s):
                
                cur=q.pop(0)
                
                if cur.left:
                #and (cur.left not in visited):
                    #visited.append(cur.left)
                    q.append(cur.left)
                if cur.right:
                    #and (cur.right not in visited):
                    #visited.append(cur.right)
                    q.append(cur.right)
                 
                tmp.append(cur.val)
            ans.append(tmp)   
        return ans
a.