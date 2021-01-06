class Balanced_110:
    """ With class variable
    def __init__(self):
        self.res = True
    
    def isBalanced(self, root: TreeNode) -> bool:
        self.height(root)
        return self.res
    
    def height(self, node):
        if node == None:
            return 0
        left_height, right_height = self.height(node.left), self.height(node.right)
        if abs(left_height - right_height) > 1:
            self.res = False
        return 1 + max(left_height, right_height)
    """



    # Without class variable
    def isBalanced(self, root: TreeNode) -> bool:
        _, res = self.helper(root)
        return res
        
    def helper(self, node):
        if node == None:
            return 0, True
        left_height, left_is_balanced = self.helper(node.left)
        right_height, right_is_balanced = self.helper(node.right)
        return 1 + max(left_height, right_height), left_is_balanced and right_is_balanced and abs(left_height - right_height) <= 1