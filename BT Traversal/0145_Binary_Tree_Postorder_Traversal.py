# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#-------------- Recursion ---------------


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #-- Postorder: left, right, node
        
        def postorder(root, stack):
            if root == None:
                return
            
            postorder(root.left, stack)
            postorder(root.right, stack)
            stack.append(root.val)
            
            
        stack=[]
        postorder(root, stack)
        
        return stack


#------------ Iteratively ----------------

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #-- Postorder: left, right, node
        
        if root == None:
            return []
        
        stack, output= [root, ], []
        
        while stack:
            root= stack.pop()
            output.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)




                
                
        return output[::-1]
            