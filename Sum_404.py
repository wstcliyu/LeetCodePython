"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

class Sum_404:
    """ My first solution
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.helper(root, False)
        
    def helper(self, root: TreeNode, left_child: bool) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val if left_child else 0
        return self.helper(root.left, True) + self.helper(root.right, False)
    """



    # Solution
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.sumOfLeftLeaves(root.right) + (root.left.val if root.left and not root.left.left and not root.left.right else self.sumOfLeftLeaves(root.left))
