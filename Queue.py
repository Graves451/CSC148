class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

obj1 = Queue()
obj1.insert(1)
obj1.insert(2)
obj1.insert(5)
print(obj1.pop())
print(obj1.pop())
print(obj1.pop())
print(obj1.pop())