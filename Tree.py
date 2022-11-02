class Tree:
    def __init__(self, root, subtrees):
        self._root = root
        self._subtrees = subtrees

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

t2 = Tree(3, [Tree(4, []), Tree(1, [])])
print(str(t2))