"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

class Subtree_572:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def toString(root: TreeNode) -> str:
            if not root:
                return "X"
            return "#" + str(root.val) + "," + toString(root.left) + "," + toString(root.right)
        return toString(t) in toString(s)
    


    """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def equals(s: TreeNode, t: TreeNode) -> bool:
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and equals(s.left, t.left) and equals(s.right, t.right)
        if not s:
            return equals(s, t)
        return equals(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    """
