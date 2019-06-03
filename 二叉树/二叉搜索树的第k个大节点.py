class solution():
    def kthnode(self, root, k):
        self.arr = []
        inorder(root)
        return arr[-k]

    def inorder(self, root):
        if not root:
            return
        inorder(root.left)
        self.arr.append = root
        inorder(root.right)
