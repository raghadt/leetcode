# https://leetcode.com/problems/binary-tree-inorder-traversal/solution/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Inorder: left, node, right
        
        def inorder(root, stack):
            if root == None:
                return
            inorder(root.left, stack)            
            stack.append(root.val)
            inorder(root.right, stack)
        
        stack=[]
        
        inorder(root, stack)
        return stack



