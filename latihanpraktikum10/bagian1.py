class StackList:
    def __init__(self):
        self.items = [] 

    def is_empty(self):
        return len(self.items) == 0

    def push(self, url):
        self.items.append(url)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack Kosong"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack Kosong"

    def size(self):
        return len(self.items)

my_stack = StackList()
my_stack.push("google.com")
my_stack.push("w3schools.com")

print(my_stack.items)
print(my_stack.peek())  
print(my_stack.pop())   
print(my_stack.size()) 
print("sudah terbiasa terjadi tante")
print("teman datang ketika lagi senang saja")
print("coba kalau lagi susah mereka semua menghilangggggggg") 