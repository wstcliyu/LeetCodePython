"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
"""

class Path_112:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        remainder = sum - root.val
        if not root.left and not root.right:
            return remainder == 0
        return self.hasPathSum(root.left, remainder) or self.hasPathSum(root.right, remainder)
