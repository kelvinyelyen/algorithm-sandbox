class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        
        # 1. Standard BST Insert
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
            
        # 2. Update Height
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        
        # 3. Get Balance Factor
        balance = self.get_balance(root)
        
        # 4. Rebalance
        # Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
        # Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        # Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
            
        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

if __name__ == "__main__":
    my_tree = AVLTree()
    root = None
    
    root = my_tree.insert(root, 10)
    root = my_tree.insert(root, 20)
    root = my_tree.insert(root, 30)
    root = my_tree.insert(root, 40)
    root = my_tree.insert(root, 50)
    root = my_tree.insert(root, 25)
    
    print("Preorder traversal of constructed AVL tree is:")
    my_tree.pre_order(root)
