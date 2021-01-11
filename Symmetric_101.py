"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.
"""

class Symmetric_101:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)
    
    def is_mirror(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and self.is_mirror(root1.left, root2.right) and self.is_mirror(root1.right, root2.left)
    
    
    
    """ Iterative (level order)
    def isSymmetric(self, root: TreeNode) -> bool:
        q = deque([root, root])
        while q:
            node1, node2 = q.popleft(), q.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            q += node1.left, node2.right, node1.right, node2.left
        return True
    """
