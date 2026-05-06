# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x,left=None,right=None):
         self.val = x
         self.left = left
         self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        
        stack=[]
        output=''
        stack.append(root)
        output+=str(root.val)

        while stack:
            tmp=stack.pop(0)
            if tmp.left:
                output+='*'+str(tmp.left.val)
                stack.append(tmp.left)
            else:
                output+='*'+'#'

            if tmp.right:
                output+='*'+str(tmp.right.val)
                stack.append(tmp.right)
            else:
                output+='*'+'#'
    
        return output

        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return None
        
        
        nodes=data.split('*')
        n=len(nodes)
        if n==1:
            if nodes[0]!="#":
                return TreeNode(nodes[0])
            else:
                return None
        queue=[]
        root=TreeNode(nodes.pop(0))
        queue.append(root)
        i=0
        while queue:
            cur=queue.pop(0)
            if nodes[i]!="#":
                left=TreeNode(nodes[i])
                cur.left=left
                print("left:",nodes[i])
                queue.append(left)
            i+=1
            
            if nodes[i]!="#":
                right=TreeNode(nodes[i])
                cur.right=right
                print("right:",nodes[i])
                queue.append(right)
            i+=1
            

        return root 
            




if __name__=='__main__':
    print("\n")
    print("Serialize Tree")
    root=TreeNode(x=1,left=TreeNode(x=2),right=TreeNode(x=3,left=TreeNode(x=4),right=TreeNode(x=5)))
    S= Codec()
    D= Codec()
    print(S.serialize(root=root))
    D.deserialize(data="1-2-3-#-#-4-5-#-#-#-#")
    ans=D.deserialize(S.serialize(root=root))
#    print(ans.left.val,ans.right)
    print(ans==root)
#    S.serialize(ans)
    
    
