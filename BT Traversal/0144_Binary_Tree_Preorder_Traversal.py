# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #Pre-order: node, left, right
        def preorder(root, stack):
            if root is None:
                return 

            stack.append(root.val)
            preorder(root.left, stack)
            preorder(root.right,stack)
            
        stack=[]
        preorder(root,stack)
        return stack
        
        