"""Tree size: CIS 211 Final Exam coding problem"""

from typing import List

class Tree:
    def size(self) -> int:
        """The size of a tree is the total number of nodes,
        including both internal and leaf nodes.
        """
        raise NotImplementedError("Did you forget to implement size?")


class Inner(Tree):
    def __init__(self, children: List[Tree]):
        self.children = children

    def size(self) -> int:
        return 0  # FIXME

    def __repr__(self) -> str:
        return repr(self.children)


class Leaf(Tree):
    def __init__(self, value: str):
        self.value = value

    def size(self) -> int:
        return 0 # FIXME

    def __repr__(self) -> str:
        return repr(self.value)

# Example 1: Tree with no children has 1 node
t1 = Inner([])
print(f"t1: {t1}, size {t1.size()}")
assert t1.size() == 1

# Example 2: A leaf is a tree with 1 node
l1 = Leaf("l1")
print(f"l1: {l1}, size {l1.size()}")
assert l1.size() == 1

#Example 3: A fuller tree
l2 = Leaf("l2")
l3 = Leaf("l3")
t2 = Inner([l2, l3])
t3 = Inner([t1, l1, t2])
print(f"t3: {t3}, size {t3.size()}")
assert t3.size() == 6

