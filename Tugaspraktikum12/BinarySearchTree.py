class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        node_baru = Node(id_buku, judul)
        if self.root is None:
            self.root = node_baru
        else:
            current = self.root
            while True:
                if id_buku < current.id_buku:
                    if current.left is None:
                        current.left = node_baru
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node_baru
                        break
                    else:
                        current = current.right
        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    def search(self, id_buku):
        current = self.root
        while current is not None:
            if id_buku == current.id_buku:
                return current
            elif id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right
        return None

    def _inorder_rekursif(self, node, hasil, counter):
        if node is not None:
            counter = self._inorder_rekursif(node.left, hasil, counter)
            counter += 1
            hasil.append((counter, node.id_buku, node.judul))
            counter = self._inorder_rekursif(node.right, hasil, counter)
        return counter

    def traversal_inorder(self):
        hasil = []
        self._inorder_rekursif(self.root, hasil, 0)
        print("\n[INFO] Koleksi Buku (In-Order Traversal):")
        for i, id_buku, judul in hasil:
            print(f"  {i}. {id_buku} - {judul}")

    def get_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    def get_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def _height_rekursif(self, node):
        if node is None:
            return -1
        tinggi_kiri = self._height_rekursif(node.left)
        tinggi_kanan = self._height_rekursif(node.right)
        return 1 + max(tinggi_kiri, tinggi_kanan)

    def height(self):
        return self._height_rekursif(self.root)


katalog = BST()

print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print("=========================================")

katalog.insert(50, "Dasar Pemrograman")
katalog.insert(30, "Struktur Data")
katalog.insert(70, "Kecerdasan Buatan")
katalog.insert(20, "Matematika Diskrit")
katalog.insert(40, "Basis Data")
katalog.insert(60, "Jaringan Komputer")
katalog.insert(80, "Sistem Operasi")

katalog.traversal_inorder()

print()
hasil_60 = katalog.search(60)
if hasil_60:
    print(f"[SEARCH] Mencari ID 60... Ditemukan! Judul: {hasil_60.judul}")
else:
    print("[SEARCH] Mencari ID 60... Data tidak ditemukan.")

hasil_100 = katalog.search(100)
if hasil_100:
    print(f"[SEARCH] Mencari ID 100... Ditemukan! Judul: {hasil_100.judul}")
else:
    print("[SEARCH] Mencari ID 100... Data tidak ditemukan.")

min_node = katalog.get_min()
max_node = katalog.get_max()
print(f"\n[STATISTIK] ID Terkecil: {min_node.id_buku}")
print(f"[STATISTIK] ID Terbesar: {max_node.id_buku}")

print(f"\n[INFO] Tinggi (Height) Tree: {katalog.height()}")
print("=========================================")
print("Simulasi Selesai!")