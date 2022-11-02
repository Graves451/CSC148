class Tree:
    def __init__(self, root, subtrees):
        self._root = root
        self._subtrees = subtrees

    def delete_item(self, target) -> bool:
        if self.is_empty():
            return False
        elif self._subtrees == []:
            if self._root == target:
                self._root = None
                return True
            return False
        else:
            if self._root == target:
                self._delete_root()
                return True
            ans = False
            for nodes in self._subtrees:
                bool = nodes.delete_item(target)
                if bool and nodes._subtrees == []:
                    self._subtrees.remove(nodes)
                    return True
                elif bool:
                    return True
            return ans

    def _delete_root(self):
        chose_tree = self._subtrees.pop()
        self._root = chose_tree._root
        self._subtrees.extend(chose_tree._subtrees)

    def is_empty(self):
        return self._root is None

    def __len__(self):
        size = 0
        if self._root:
            size += 1
        for nodes in self._subtrees:
            if not nodes.is_empty():
                size += nodes.__len__()
        return size

    def __str__(self):
        return self._str_indent(0)

    def _str_indent(self, depth: int=0) -> str:
        if self.is_empty():
            return ''
        ans = ''
        ans += " " * depth + str(self._root) + "\n"
        for nodes in self._subtrees:
            ans += nodes._str_indent(depth+1)
        return ans



"""
Return the number of items contained in this tree.
t1 = Tree(None, [])
len(t1)
>>> 0
t2 = Tree(3, [Tree(4, []), Tree(1, [])])
len(t2)
>>> 3
"""

t = Tree(10, [Tree(1, []), Tree(2, []), Tree(3, [])])  # A tree with leaves 1, 2, and 3
print(t.delete_item(1))
print(t.delete_item(2))
print(t.delete_item(3))
print(t._subtrees)
print(t._subtrees[0].is_empty() and t._subtrees[1].is_empty() and t._subtrees[2].is_empty())