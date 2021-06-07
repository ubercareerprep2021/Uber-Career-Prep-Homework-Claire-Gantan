import unittest

class tree:
    def __init__(self, root):
        self.root = root

class tree_node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

#preorder, postorder and inorder prints

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

def inorder_print(tr):
    #traverse left subtree, then root, then right subtree
    if tr.root is None:
        return
    inorder_print(tree(tr.root.left))
    print(tr.root.data)
    inorder_print(tree(tr.root.right))

def preorder_print(tr):
    #traverse root, then left subtree, then right subtree
    if tr.root is None:
        return
    print(tr.root.data)
    preorder_print(tree(tr.root.left))
    preorder_print(tree(tr.root.right))

def postorder_print(tr):
    #traverse left subtree, then right subtree, then root
    if tr.root is None:
        return
    postorder_print(tree(tr.root.left))
    postorder_print(tree(tr.root.right))
    print(tr.root.data)

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

    def test_preorder_print(self):
        two = tree_node(2, None, None)
        six_left = tree_node(5, None, None)
        six_right = tree_node(11, None, None)
        six = tree_node(6, six_left, six_right)
        left = tree_node(7, two, six)
        four = tree_node(4, None, None)
        nine = tree_node(9, four, None)
        right = tree_node(5, None, nine)
        root = tree_node(2, left, right)
        test_tree = tree(root)
        print("preorder starting, should be 2 7 2 6 5 11 5 9 4")
        preorder_print(test_tree)

    def test_postorder_print(self):
        two = tree_node(2, None, None)
        six_left = tree_node(5, None, None)
        six_right = tree_node(11, None, None)
        six = tree_node(6, six_left, six_right)
        left = tree_node(7, two, six)
        four = tree_node(4, None, None)
        nine = tree_node(9, four, None)
        right = tree_node(5, None, nine)
        root = tree_node(2, left, right)
        test_tree = tree(root)
        print("postorder starting, should be 2 5 11 6 7 4 9 5 2")
        postorder_print(test_tree)

    def test_inorder_print(self):
        two = tree_node(2, None, None)
        six_left = tree_node(5, None, None)
        six_right = tree_node(11, None, None)
        six = tree_node(6, six_left, six_right)
        left = tree_node(7, two, six)
        four = tree_node(4, None, None)
        nine = tree_node(9, four, None)
        right = tree_node(5, None, nine)
        root = tree_node(2, left, right)
        test_tree = tree(root)
        print("inorder starting, should be 2 7 5 6 11 2 5 4 9")
        inorder_print(test_tree)

if __name__ == '__main__':
    unittest.main()

#Ex 1-3:
#TIMING (without retyping tree class and example case)
#print: 11 min
#breadth_first_print = 9 min
#levels = 6 min
# reflection: was able to use a lot of recursion which was super helpful! I was not sure whether we were supposed to use the tree class given in the spec or not, but it was how I would have implemented it as well, so I just studied and retyped it.
#extra practice: preorder, postorder and inorder prints (with test cases written first)
#example tree from: https://www.google.com/url?sa=i&url=https%3A%2F%2Ftech.paayi.com%2Fpython-tree-data-structures&psig=AOvVaw0F6fGCiTTjtPLLNFFLUzXX&ust=1623184834967000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCICyzvGwhvECFQAAAAAdAAAAABAI
#TIMING: writing tests: 8 min, writing code: 13 min
