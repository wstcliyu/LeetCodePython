class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Binary_156:
    # Most voted solution: Iterative
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        curr, next, prev, temp = root, None, None, None
        while curr is not None:
            next = curr.left
            curr.left = temp
            temp = curr.right
            curr.right = prev
            prev = curr
            curr = next
        return prev


    # Most voted solution: Recursive
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if root is None or root.left is None:
            return root
        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None
        return newRoot


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Binary_156()
    newRoot = solution.upsideDownBinaryTree(root)
    print(newRoot.val)
    print(newRoot.left.val)
    print(newRoot.right.val)
    print(newRoot.right.left.val)
    print(newRoot.right.right.val)