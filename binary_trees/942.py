# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            val = postorder.pop()
            root = TreeNode(val)
            index_match = inorder.index(val)
            root.right = helper(index_match + 1, in_right)
            root.left = helper(in_left, index_match - 1)
            return root
        return helper(0, len(inorder) - 1)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        
        H = {val:idx for idx, val in enumerate(inorder)}
        stack = []
        root = None
        for node_val in reversed(postorder):
            node = TreeNode(node_val)
            if not stack:
                # only occurs for the postorder[-1], which is the root
                root = node
                stack.append(node)
            else:
                parent = stack[-1]
                if H[node.val] > H[parent.val]:
                    # right subtree of the previous node
                    parent.right = node
                else:
                    # left subtree of the previous node
                    while stack and H[node.val] < H[stack[-1].val]:
                        parent = stack.pop()
                    parent.left = node
                stack.append(node)
        
        return root        