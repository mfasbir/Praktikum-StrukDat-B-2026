class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1 & 3. Fungsi insert_tail()
    def insert_tail(self, nama):
        new_node = Node(nama)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    # 2. Fungsi print_antrian()
    def print_antrian(self):
        if not self.head:
            print("Antrian Kosong")
            return
        curr = self.head
        antrian = []
        while True:
            antrian.append(curr.nama)
            curr = curr.next
            if curr == self.head:
                break
        print(" -> ".join(antrian) + " -> (Kembali ke " + self.head.nama + ")")

    # 4. Fungsi delete_head()
    def delete_head(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        
        last = self.head
        while last.next != self.head:
            last = last.next
        
        last.next = self.head.next
        self.head = self.head.next

# Menjalankan Program
cll = CircularLinkedList()
cll.insert_tail("Andi")
cll.insert_tail("Budi")
cll.insert_tail("Citra")
cll.insert_tail("Dina")

print("Antrian Awal:")
cll.print_antrian()

print("\n--- Edo datang dan masuk antrian ---")
cll.insert_tail("Eo")
cll.print_antrian()

print("\n--- Andi selesai dilayani ---")
cll.delete_head()
cll.print_antrian()