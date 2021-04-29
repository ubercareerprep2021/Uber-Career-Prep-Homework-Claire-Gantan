###TIMING: 60 minutes so far
import unittest

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    # def setNext(self, next):
    #     self.next = next
    # def setVal(self, val):
    #     self.value = val

class linked_list:
    def __init__(self):
        self.head = None
        self.sizes = 0

    def push(self, node):
        temp = self.head
        self.head = node
        node.next = temp
        self.sizes+=1

    def pop(self):
        if self.head is None:
            return None
        temp, self.head = self.head, self.head.next
        self.sizes-=1
        return temp

    def size(self):
        return self.sizes

    def insert(self, index, node):
        temp_head = self.head
        for i in range(index):
            if temp_head is None:
                return
            temp_head = temp_head.next
        temp_next = temp_head.next
        temp_head.next = node
        node.next = temp_next
        self.sizes += 1

    def remove(self, index):
        temp_head = self.head
        for i in range(index):
            if temp_head is None:
                return
            temp_prev = temp_head
            temp_head = temp_head.next
        if temp_head is None:
            return
        temp_prev.next = temp_head.next
        self.sizes -= 1

    def elementAt(self, index):
        temp_head = self.head
        for i in range(index):
            if temp_head is None:
                return
            temp_head = temp_head.next
        if temp_head is None:
            return
        return temp_head

    def printList(self): #prints or returns string cuz it says void in the spec??
        values = ""
        temp_head = self.head
        for i in range(self.sizes):
            values = values+str(temp_head.value)+" "
            temp_head = temp_head.next
        print(values)

    def isPalindrome(self):

    def hasCycle(self):



class UnitTests(unittest.TestCase):
    def testPushBackAddsOneNode(self):
        link = linked_list()
        n = Node(3,None)
        link.push(n)
        test = Node(4, None)
        link.push(test)
        self.assertEqual(link.size(),2)
        self.assertEqual(link.elementAt(0).value,4)
        self.assertEqual(link.elementAt(1).value,3)
        self.assertEqual(link.elementAt(2),None)
        #self.assertTrue(myQueue.isEmpty())

    def testPopBackRemovesCorrectNode(self):
        link = linked_list()
        n = Node(3,None)
        link.push(n)
        test = Node(4, None)
        link.push(test)
        link.pop()
        self.assertEqual(link.size(),1)
        self.assertEqual(link.elementAt(0).value,3)
        self.assertEqual(link.elementAt(1),None)

    def testEraseRemovesCorrectNode(self):
        link = linked_list()
        a = Node(9,None)
        link.push(a)
        b = Node(8, None)
        link.push(b)
        c = Node(5, None)
        link.push(c)
        self.assertEqual(link.elementAt(0).value,5)
        self.assertEqual(link.elementAt(1).value,8)
        self.assertEqual(link.elementAt(2).value,9)
        self.assertEqual(link.elementAt(3),None)
        link.remove(1)
        self.assertEqual(link.size(), 2)
        self.assertEqual(link.elementAt(0).value,5)
        self.assertEqual(link.elementAt(1).value,9)
        self.assertEqual(link.elementAt(2),None)
        link.remove(1)
        self.assertEqual(link.size(), 1)
        self.assertEqual(link.elementAt(0).value,5)
        self.assertEqual(link.elementAt(1),None)

    def testEraseDoesNothingIfNoNode(self):
        link = linked_list()
        link.remove(0)
        self.assertEqual(link.size(), 0)
        a = Node(4,None)
        link.push(a)
        self.assertEqual(link.elementAt(0).value,4)
        self.assertEqual(link.elementAt(1),None)
        self.assertEqual(link.size(), 1)
        link.remove(3)
        self.assertEqual(link.elementAt(0).value,4)
        self.assertEqual(link.elementAt(1),None)
        self.assertEqual(link.size(), 1)

    def testElementAtReturnNode(self):
        link = linked_list()
        a = Node(9,None)
        link.push(a)
        b = Node(8, None)
        link.push(b)
        c = Node(5, None)
        link.push(c)
        self.assertEqual(link.elementAt(0).value,5)
        self.assertEqual(link.elementAt(1).value,8)
        self.assertEqual(link.elementAt(2).value,9)
        self.assertEqual(link.elementAt(3),None)
        d = link.elementAt(0)
        self.assertEqual(d.next.value, 8)

    def testElementAtReturnsNoNodeIfIndexDoesNotExist(self):
        link = linked_list()
        a = Node(9,None)
        link.push(a)
        b = Node(8, None)
        link.push(b)
        c = Node(5, None)
        link.push(c)
        self.assertEqual(link.elementAt(0).value,5)
        self.assertEqual(link.elementAt(1).value,8)
        self.assertEqual(link.elementAt(2).value,9)
        self.assertEqual(link.elementAt(3),None)
        d = link.elementAt(5)
        self.assertEqual(d, None)

    def testSizeReturnsCorrectSize(self):
        link = linked_list()
        self.assertEqual(link.size(),0)
        a = Node(9,None)
        link.push(a)
        self.assertEqual(link.size(),1)
        b = Node(8, None)
        link.push(b)
        self.assertEqual(link.size(),2)
        c = Node(5, None)
        link.push(c)
        self.assertEqual(link.size(),3)

if __name__ == '__main__':
    unittest.main()
