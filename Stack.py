class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(len(self.items)-1)


obj1 = Stack()
obj1.insert(1)
obj1.insert(2)
obj1.insert(3)
print(obj1.pop())
print(obj1.pop())