# from collections import deque

"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

class Invert_226:
    """ Recursive
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    """
    
    
    
    """ Iterative with queue (level order)
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        q = collections.deque([root])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
    """
    
    
    
    """ Iterative with stack #1 (pre order)
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
    """
    
    
    
    """ Iterative with stack #2 (pre order)
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = []
        p = root
        while stack or p:
            if p:
                stack.append(p)
                p.left, p.right = p.right, p.left
                p = p.left
            else:
                p = stack.pop().right
        return root
