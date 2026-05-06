"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return None
        
        queue=[]
        queue.append(root)
        
        while queue:
            n=len(queue)
            if n==1:
                s=queue.pop()
                s.next=None
                if s.right:
                    queue.append(s.right)
                    
                if s.left:
                    queue.append(s.left)
            else:
                prev=None
                for _ in range(n):
                    s=queue.pop(0)
                    s.next=prev
                    prev=s
                    
                    if s.right:
                        queue.append(s.right)
                    if s.left:
                        queue.append(s.left)
        return root

        