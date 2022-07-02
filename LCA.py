class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        # Code here
        if root==None:
            return None
        
        l_ = self.lca(root.left, n1, n2)
        r_ = self.lca(root.right, n1, n2)
        
        if root.data==n1 or root.data ==n2:
            return root
        if l_ and r_:
            return root
        elif l_:
            return l_
        elif r_:
            return r_
        else:
            return None
