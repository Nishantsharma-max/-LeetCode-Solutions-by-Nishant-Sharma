# Same Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        p_res=[]
        q_res=[]
        self.helper(p,p_res)
        self.helper(q,q_res)
        if p_res==q_res:
            return True
        else:
            return False

    def helper(self,node,res):
        if not node:
            res.append("meo")
            return 
        res.append(node.val)
        self.helper(node.left,res)
        self.helper(node.right,res)    
    

        