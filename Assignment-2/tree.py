import unittest

class tree:
    def __init__(self, root):
        self.root = root

class tree_node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def print_tree(tr):
    if tr.root is None:
        return
    if tr.root.left is not None:
        print_tree(tree(tr.root.left))
    print(tr.root.data)
    print_tree(tree(tr.root.right))

def breadth_first_print(tr):
    if tr.root is None:
        return
    print(tr.root.data)
    breadth_first_print(tree(tr.root.left))
    breadth_first_print(tree(tr.root.right))

def num_levels(tr):
    if tr.root is None:
        return 0
    else:
        return 1 + max(num_levels(tree(tr.root.left)), num_levels(tree(tr.root.right)))

class UnitTests(unittest.TestCase):
    def test_print(self):
        left_child = tree_node(6, None, None)
        right_child = tree_node(3, None, None)
        left = tree_node(7, None, None)
        right = tree_node(17, left_child, right_child)
        root = tree_node(1, left, right)
        my_tree = tree(root)
        print("left first starting")
        print_tree(my_tree)

    def test_breadth_print(self):
        left_child = tree_node(6, None, None)
        right_child = tree_node(3, None, None)
        left = tree_node(7, None, None)
        right = tree_node(17, left_child, right_child)
        root = tree_node(1, left, right)
        my_tree = tree(root)
        print("breadth first starting")
        breadth_first_print(my_tree)

    def test_num_levels(self):
        left_child = tree_node(6, None, None)
        right_child = tree_node(3, None, None)
        left = tree_node(7, None, None)
        right = tree_node(17, left_child, right_child)
        root = tree_node(1, left, right)
        my_tree = tree(root)
        second_tree = tree(right)
        self.assertEqual(num_levels(my_tree),3)
        self.assertEqual(num_levels(second_tree),2)

if __name__ == '__main__':
    unittest.main()

#Ex 1-3:
#TIMING (without retyping tree class and example case)
#print: 11 min
#breadth_first_print = 9 min
#levels = 6 min
# reflection: was able to use a lot of recursion which was super helpful! I was not sure whether we were supposed to use the tree class given in the spec or not, but it was how I would have implemented it as well, so I just studied and retyped it.
