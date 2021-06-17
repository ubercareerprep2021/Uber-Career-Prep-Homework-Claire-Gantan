import unittest


class tree_node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class binary_search_tree:
    def __init__(self, root):
        self.root = root

    # Inserts a key into this binary search tree.
    # If there are n nodes in the tree, then the average runtime of this method should be log(n).
    # @param key The key to insert.
    def insert(self, key):
        temp = self.root
        if temp is None:
            self.root = tree_node(key, None, None)
            return
        while temp is not None:
            if temp.data == key:
                return
            elif temp.data < key:
                if temp.right is None:
                    temp.right = tree_node(key, None, None)
                    return
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = tree_node(key, None, None)
                    return
                temp = temp.left
        temp = tree_node(key, None, None)

    # Checks whether or not a key exists in this binary search tree.
    # If there are n nodes in the tree, then the average runtime of this method should be log(n).
    # @param key The key to check for.
    # @return true if the key is present in this binary search tree, false otherwise.
    def find(self, key):
        temp = self.root
        while temp is not None:
            if temp.data == key:
                return True
            elif temp.data > key:
                temp = temp.left
            else:
                temp = temp.right
        return False


class UnitTests(unittest.TestCase):
    def test_insert(self):
        root = tree_node(2, None, None)
        test_tree = binary_search_tree(root)
        test_tree.insert(4)
        test_tree.insert(1)
        self.assertEqual(test_tree.root.data, 2)
        self.assertEqual(test_tree.root.left.data, 1)
        self.assertEqual(test_tree.root.right.data, 4)
        test_tree.insert(5)
        test_tree.insert(3)
        self.assertEqual(test_tree.root.right.left.data, 3)
        self.assertEqual(test_tree.root.right.right.data, 5)

    def test_find_basic(self):
        root = tree_node(2, None, None)
        test_tree = binary_search_tree(root)
        test_tree.insert(4)
        test_tree.insert(1)
        self.assertTrue(test_tree.find(4))
        self.assertFalse(test_tree.find(3))
        test_tree.insert(5)
        self.assertEqual(test_tree.root.right.right.data, 5)
        self.assertTrue(test_tree.find(5))
        self.assertFalse(test_tree.find(3))

    def test_empty(self):
        empty_tree = binary_search_tree(None)
        self.assertFalse(empty_tree.find(0))

    def test_insert_into_empty(self):
        empty_tree = binary_search_tree(None)
        self.assertFalse(empty_tree.find(589))
        empty_tree.insert(589)
        self.assertTrue(empty_tree.find(589))


if __name__ == '__main__':
    unittest.main()

#TIMING:
#ex 4: tests: 5 min, writing code: 23 min
