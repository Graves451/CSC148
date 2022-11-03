class BinaryTree:
    def __init__(self, root):
        if root is None:
            self._root = None
            self._right = None
            self._left = None
        else:
            self._root = root
            self._right = BinaryTree(None)
            self._left = BinaryTree(None)

    def is_empty(self):
        return self._root is None

    def height(self):
        return self.dfs()

    def dfs(self) -> int:
        if self.is_empty():
            return 0
        return max(1 + self._right.dfs(), self._left.dfs())

    def insert(self, item):
        if self.is_empty():
            self._root = BinaryTree(item)
        elif self._root == item:
            return
        elif self._root < item:
            if self._right.is_empty():
                self._right = BinaryTree(item)
            else:
                self._right.insert(item)
        elif self._root > item:
            if self._left.is_empty():
                self._left = BinaryTree(item)
            else:
                self._left.insert(item)

    def delete(self, item):
        if self.is_empty():
            return
        elif self._root == item:
            self.delete_root()
        elif self._root > item:
            self._left.delete(item)
        else:
            self._right.delete(item)

    def delete_root(self):





    def __contains__(self, item) -> bool:
        if self.is_empty():
            return False
        elif self._root == item:
            return True
        elif self._root > item:
            return self._right.__contains__(item)
        else:
            return self._left.__contains__(item)

    def __str__(self):
        return self.str_indent(0)

    def str_indent(self, depth):
        ans = ""
        if self.is_empty():
            return ans
        ans += f"{depth*' '}{self._root}\n"
        ans += self._right.str_indent(depth + 1)
        ans += "\n"
        ans += self._left.str_indent(depth + 1)
        return ans

obj1 = BinaryTree(10)
obj1.insert(2)
obj1.insert(15)
obj1.insert(20)
obj1.insert(30)
obj1.insert(6)
print(obj1.height())
print(str(obj1))