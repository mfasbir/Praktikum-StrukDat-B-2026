class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node("A")

        self.root.left = Node("B")
        self.root.right = Node("C")

        self.root.left.left = Node("D")
        self.root.left.right = Node("E")

        self.root.right.right = Node("F")

    def traverse_preorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.data)
            self.traverse_preorder(node.left, result)
            self.traverse_preorder(node.right, result)
        return result

    def traverse_inorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.traverse_inorder(node.left, result)
            result.append(node.data)
            self.traverse_inorder(node.right, result)
        return result

    def traverse_postorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.traverse_postorder(node.left, result)
            self.traverse_postorder(node.right, result)
            result.append(node.data)
        return result

    def get_leaf_nodes(self, node, result=None):
        if result is None:
            result = []
        if node:
            if node.left is None and node.right is None:
                result.append(node.data)
            self.get_leaf_nodes(node.left, result)
            self.get_leaf_nodes(node.right, result)
        return result

tree = BinaryTree()

print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print("======================================")
print("[INFO] Membangun Struktur Gudang...")
tree.insert_manual()
print("[INFO] Struktur berhasil dibuat.")
print()

preorder   = tree.traverse_preorder(tree.root)
inorder    = tree.traverse_inorder(tree.root)
postorder  = tree.traverse_postorder(tree.root)
leaf_nodes = tree.get_leaf_nodes(tree.root)

print("HASIL AUDIT:")
print("1. Pre-Order  :", " - ".join(preorder))
print("2. In-Order   :", " - ".join(inorder))
print("3. Post-Order :", " - ".join(postorder))
print()
print("[DATA] Gudang Ujung (Leaf Nodes):", ", ".join(leaf_nodes))
print("======================================")
print("Audit Selesai!")