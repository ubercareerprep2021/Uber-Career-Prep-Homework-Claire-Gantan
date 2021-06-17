import unittest
from csv import reader
import time

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
                temp = temp.left
        temp = tree_node(key, val, None, None)

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
        if self.book is None:
            return -1
        return self.book.find(name)

class UnitTests(unittest.TestCase):
    def test_short_list(self):
        book = list_phone_book()
        book.insert("ABC",111111111)
        self.assertEqual(book.size(),1)
        self.assertEqual(book.find("ABC"),111111111)
        self.assertEqual(book.find("DEF"), -1)
        book.insert("DEF",222222222)
        self.assertEqual(book.size(),2)
        self.assertEqual(book.find("ABC"),111111111)
        self.assertEqual(book.find("DEF"), 222222222)

    def test_short_bst(self):
        book = bst_phone_book()
        book.insert("ABC",111111111)
        self.assertEqual(book.size(),1)
        self.assertEqual(book.find("ABC"),111111111)
        self.assertEqual(book.find("DEF"), -1)
        book.insert("DEF",222222222)
        self.assertEqual(book.size(),2)
        self.assertEqual(book.find("ABC"),111111111)
        self.assertEqual(book.find("DEF"), 222222222)

    def test_empty_bst(self):
        book = bst_phone_book()
        self.assertEqual(book.find("DEF"), -1)

    def test_empty_list(self):
        book = list_phone_book()
        self.assertEqual(book.find("DEF"), -1)

    def test_same_vals_bst(self):
        book = bst_phone_book()
        book.insert("one",123)
        book.insert("two",123)
        self.assertEqual(book.find("one"), 123)
        self.assertEqual(book.find("two"), 123)

    def test_same_vals_list(self):
        book = list_phone_book()
        book.insert("one",123)
        book.insert("two",123)
        self.assertEqual(book.find("one"), 123)
        self.assertEqual(book.find("two"), 123)

    def test_big_list(self):
        book = list_phone_book()
        with open("data.csv", "r") as read_obj:
            txt = reader(read_obj)
            start = time.time()
            for line in txt:
                book.insert(line[0],line[1])
            end = time.time()
        print("List Phonebook:")
        print("Insert took "+str((end-start)*1000)+" milliseconds.")
        print("The size of the phone book is "+str(book.size()))
        with open("search.txt") as txt:
            start = time.time()
            count = 0
            for line in txt:
                count += 1
                if book.find(line[:-1]) == -1: #[:-1] gets rid of the newline at the end of the readline
                    raise SystemExit('Line not found')
            end = time.time()
        print("Find() was called "+str(count)+" times.")
        print("Find took "+str((end-start)*1000)+" milliseconds.")
        print()

    def test_big_bst(self):
        temp_book = bst_phone_book()
        with open("data.csv", "r") as read_obj:
            txt = reader(read_obj)
            start = time.time()
            for line in txt:
                temp_book.insert(line[0], line[1])
            end = time.time()
        print("BST Phonebook:")
        print("Insert took "+str((end-start)*1000)+" milliseconds.")
        print("The size of the phone book is "+str(temp_book.size()))
        with open("search.txt") as txt:
            start = time.time()
            count = 0
            for line in txt:
                count += 1
                if temp_book.find(line[:-1]) == -1: #[:-1] gets rid of the newline at the end of the readline
                    print(line[:-1])
                    raise SystemExit('Line not found')
            end = time.time()
        print("Find() was called "+str(count)+" times.")
        print("Find took "+str((end-start)*1000)+" milliseconds.")
        print()

    #recreating error found when using the text file to debug
    def test_insert_bst(self):
        temp_book = bst_phone_book()
        temp_book.insert('1fours','456789123')
        temp_book.insert('4ones', '123456789')
        temp_book.insert('2twos', '234567891')
        temp_book.insert('1threes','345678912')
        temp_book.insert('rand-123', '012938475')
        self.assertEqual(temp_book.find('4ones'),'123456789')
        self.assertEqual(temp_book.find('2twos'),'234567891')
        self.assertEqual(temp_book.find('1threes'),'345678912')
        self.assertTrue(temp_book.find('rand-123'),'012938475')
        self.assertEqual(temp_book.find('1fours'),'456789123')

if __name__ == '__main__':
    unittest.main()


#TIMING:
#ex 5: code writing: 7 min list AND 8 min bst, tests: 2 min
#ex 6: code writing:, tests: 1:29-1:55
#needed to check how to read lines, error printing and time code in python
