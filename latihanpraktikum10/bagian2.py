class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 

    def is_empty(self):
        return self.top is None

    def push(self, url):

        new_node = Node(url)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
    
        popped_url = self.top.url
        self.top = self.top.next
        self.count -= 1
        return popped_url

    def peek(self):
        if self.is_empty():
            return None
        return self.top.url

    def size(self):
        return self.count
    
browser = StackLinkedList()
browser.push("google.com")
browser.push("github.com")
print(f"Halaman aktif: {browser.peek()}")
print(f"Kembali dari: {browser.pop()}")    
print(f"Halaman sekarang: {browser.peek()}") 

