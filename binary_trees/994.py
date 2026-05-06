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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None
        
        queue=[]
        queue.append(root)
        
        while queue:
            n=len(queue)
            if n==1:
                s=queue.pop()
                s.next=None
                if s.right and s.left:
                    queue.append(s.right)
                    queue.append(s.left)
            else:
                prev=None
                for _ in range(n):
                    s=queue.pop(0)
                    s.next=prev
                    prev=s
                    
                    if s.right and s.left:
                        queue.append(s.right)
                        queue.append(s.left)
        return root


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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        self.walk(root)
        return root

    def walk(self, root):
        if root.left== None and root.right== None:
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.walk(root.left)
        self.walk(root.right)


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self,root):
        if not root:
            return
        if (root.left):
            root.left.next = root.right
            if(root.next):
                root.right.next = root.next.left
            else:
                root.right.next = None
        self.connect(root.left)
        self.connect(root.right)
        return root
	

