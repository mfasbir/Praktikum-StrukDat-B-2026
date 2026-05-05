class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # 2. Fungsi insert_tail()
    def insert_tail(self, judul, pengarang):
        new_node = Node(judul, pengarang)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # 3. Fungsi print_forward()
    def print_forward(self):
        print("Daftar Buku (Forward):")
        curr = self.head
        while curr:
            print(f"- {curr.judul} ({curr.pengarang})")
            curr = curr.next
        print()

    # 3. Fungsi print_backward()
    def print_backward(self):
        print("Daftar Buku (Backward):")
        curr = self.head
        if not curr: return
        while curr.next:
            curr = curr.next
        while curr:
            print(f"- {curr.judul} ({curr.pengarang})")
            curr = curr.prev
        print()

    # 4. Fungsi delete_by_judul()
    def delete_by_judul(self, judul):
        curr = self.head
        while curr:
            if curr.judul == judul:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                
                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next

# Menjalankan Program
dll = DoubleLinkedList()
dll.insert_tail("Laskar Pelangi", "Andrea Hirata")
dll.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
dll.insert_tail("Sang Pemimpi", "Andrea Hirata")

dll.print_forward()
dll.print_backward()

print("--- Menghapus Bumi Manusia ---")
dll.delete_by_judul("Bumi Manusia")
dll.print_forward()