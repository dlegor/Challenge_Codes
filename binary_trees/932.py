# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import namedtuple


class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        Status=namedtuple('Status',('num_target_nodes','ancestor'))
            
        def lca_helper(root:'TreeNode',p:'TreeNode',q:'TreeNode'):
            
            if not root:
                return Status(num_target_nodes=0,ancestor=None)
            
            left_result=lca_helper(root.left,p,q)
            if left_result.num_target_nodes==2:
                return left_result
            right_result=lca_helper(root.right,p,q)
            if right_result.num_target_nodes==2:
                return right_result
            
            num_target_nodes=(left_result.num_target_nodes+
                              right_result.num_target_nodes+
                             (p,q).count(root))
            if num_target_nodes==2:
                tree=root
            else:
                tree=None
            
            return Status(num_target_nodes,tree)
            
        return lca_helper(root,p,q).ancestor
            
        if root is None:
            return None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left and right) or (root == p) or (root == q):
            return root

        return left or right