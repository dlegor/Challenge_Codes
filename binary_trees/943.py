# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None
        
        H={val:idx for idx,val in enumerate(inorder)}
        
        stack=[]
        root=None
        
        for node_val in preorder:
            node=TreeNode(val=node_val)
            
            if not stack:
                root=node
                stack.append(node)
            else:
                parent=stack[-1]
                if H[node.val]<H[parent.val]:
                    parent.left=node
                else:
                    
                    while stack and H[node.val]>H[stack[-1].val]:
                        parent=stack.pop()
                    parent.right=node
                stack.append(node)
        
        return root
a