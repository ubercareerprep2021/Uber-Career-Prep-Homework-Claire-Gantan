import unittest

#adding bst coded in ex 4, edited to have key value pairs
class tree_node:
    def __init__(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class binary_search_tree:
    def __init__(self, root):
        self.root = root

    def insert(self, key, val):
        temp = self.root
        while temp is not None:
            if temp.key == key:
                return
            elif temp.key < key:
                if temp.right is None:
                    temp.right = tree_node(key, val, None, None)
                    return
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = tree_node(key, val, None, None)
                    return
                temp = temp.right
        temp = tree_node(key, None, None)

    def find(self, key):
        temp = self.root
        while temp is not None:
            if temp.key == key:
                return temp.val
            elif temp.key > key:
                temp = temp.left
            else:
                temp = temp.right
        return -1

class phone_book:
    def size(self):
        pass
    def insert(self, name, number):
        pass
    def find(self, name):
        pass

class list_phone_book(phone_book):
    def __init__(self):
        self.names = list()
        self.numbers = list()
    def size(self):
        return len(self.names)
    def insert(self, name, number):
        self.names.append(name)
        self.numbers.append(number)
    def find(self, name):
        if name in self.names:
            return self.numbers[self.names.index(name)]
        return -1

class bst_phone_book(phone_book):
    def __init__(self):
        self.book = None
        self.len = 0
    def size(self):
        return self.len
    def insert(self, name, number):
        if self.book is None:
            root = tree_node(name, number, None, None)
            self.book = binary_search_tree(root)
        else:
            self.book.insert(name, number)
        self.len += 1
    def find(self, name):
        return self.book.find(name)

class UnitTests(unittest.TestCase):
    def test_list(self):
        book = list_phone_book()
        book.insert("ABC",111111111)
        self.assertEqual(book.size(),1)
        self.assertEqual(book.find("ABC"),111111111)
        self.assertEqual(book.find("DEF"), -1)
        book.insert("DEF",222222222)
        self.assertEqual(book.size(),2)
        self.assertEqual(book.find("ABC"),111111111)
        self.assertEqual(book.find("DEF"), 222222222)
    def test_bst(self):
        book = bst_phone_book()
        book.insert("ABC",111111111)
        self.assertEqual(book.size(),1)
        self.assertEqual(book.find("ABC"),111111111)
        self.assertEqual(book.find("DEF"), -1)
        book.insert("DEF",222222222)
        self.assertEqual(book.size(),2)
        self.assertEqual(book.find("ABC"),111111111)
        self.assertEqual(book.find("DEF"), 222222222)


if __name__ == '__main__':
    unittest.main()


#TIMING: ex 5: code writing: 7 min list AND 8 min bst, tests: 2 min
