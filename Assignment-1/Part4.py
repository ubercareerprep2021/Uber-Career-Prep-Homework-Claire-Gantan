
import unittest

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

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
        #thought process: reverse first half of list and then compare to the second half
        temp_list = linked_list()
        temp_head = self.head
        for i in range(self.sizes//2):
            temp_list.push(Node(temp_head.value,None))
            temp_head = temp_head.next
        first_head = temp_list.head
        second_head = temp_head
        if self.sizes % 2 == 1:
            second_head = second_head.next
        for i in range(self.sizes//2):
            if (first_head is None) or (second_head is None):
                return False
            if first_head.value != second_head.value:
                return False
            first_head, second_head = first_head.next, second_head.next
        return True

    def hasCycle(self):
        seen = set()
        temp_head = self.head
        for i in range(self.sizes):
            if temp_head in seen:
                return True
            seen.add(temp_head)
            temp_head = temp_head.next
        return False


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

    def testHasCycle(self):
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
        self.assertFalse(link.hasCycle())
        link.push(a)
        # link.printList()
        self.assertEqual(link.elementAt(0).value,9)
        self.assertEqual(link.elementAt(1).value,5)
        self.assertEqual(link.elementAt(2).value,8)
        self.assertEqual(link.elementAt(3).value,9)
        self.assertTrue(link.hasCycle())

    def testPalindrome(self):
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
        d = Node(8, None)
        link.push(d)
        e = Node(9, None)
        link.push(e)
        self.assertEqual(link.elementAt(0).value,9)
        self.assertEqual(link.elementAt(1).value,8)
        self.assertEqual(link.elementAt(2).value,5)
        self.assertEqual(link.elementAt(3).value,8)
        self.assertEqual(link.elementAt(4).value,9)
        self.assertEqual(link.elementAt(5),None)
        self.assertTrue(link.isPalindrome())

if __name__ == '__main__':
    unittest.main()

###TIMING: 90 minutes for everything (including palindrome and test cases)
##not sure if there is a better way to do palindrome
