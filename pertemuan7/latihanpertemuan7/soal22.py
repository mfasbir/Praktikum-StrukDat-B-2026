class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntreanLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, nama_pasien, posisi):
        new_node = Node(nama_pasien)
        
        if posisi <= 1 or not self.head:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 1
        
        while current.next is not None and count < posisi - 1:
            current = current.next
            count += 1
            
        new_node.next = current.next
        current.next = new_node

    def tampilkan_antrean(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        print("Antrean Pasien:", result)

rs_antrean = AntreanLinkedList()
rs_antrean.insert_at_position("Pasien A (Stabil)", 1)
rs_antrean.insert_at_position("Pasien B (Stabil)", 2)
rs_antrean.insert_at_position("Pasien C (Stabil)", 3)

rs_antrean.insert_at_position("Pasien DARURAT X", 2)

rs_antrean.insert_at_position("Pasien Terlambat Y", 10)

rs_antrean.tampilkan_antrean()