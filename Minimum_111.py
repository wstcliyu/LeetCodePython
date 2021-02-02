"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""

class Minimum_111:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_min_depth, right_min_depth = self.minDepth(root.left), self.minDepth(root.right)
        if not left_min_depth or not right_min_depth:
            return 1 + left_min_depth + right_min_depth
        return 1 + min(left_min_depth, right_min_depth)



    # level order
    """
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        depth = 1
        while q:
            level = []
            for node in q:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            depth += 1
            q = level
        return depth
    """
