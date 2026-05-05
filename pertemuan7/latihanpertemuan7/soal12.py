class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HistoryLinkedList:
    def __init__(self):
        self.head = None

    def tambah_pencarian_linked(self, keyword):
        new_node = Node(keyword)
        new_node.next = self.head
        self.head = new_node

    def tampilkan_history(self):
        current = self.head
        history_list = []
        while current:
            history_list.append(current.data)
            current = current.next
        print("Riwayat (Linked List):", history_list)

history_ll = HistoryLinkedList()
history_ll.tambah_pencarian_linked("python.org")
history_ll.tambah_pencarian_linked("google.com")
history_ll.tambah_pencarian_linked("github.com")

history_ll.tampilkan_history()