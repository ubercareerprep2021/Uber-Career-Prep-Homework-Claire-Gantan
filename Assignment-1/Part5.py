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

#Additions for part 5 here:
#Timing: 9 min (iterative) // 36 min (stack) // 34 min (recursive)

#if you are creating a new linked list would it still have O(1) space complexity??
def iterative_reverse(c):
    temp_head = c.head
    result = linked_list()
    while temp_head is not None:
        n = Node(temp_head.value, None)
        result.push(n)
        temp_head = temp_head.next
    return result

#started with a node reference for this method
def recursive_reverse(node_i):
    if node_i is None:
        return None
    if node_i.next is None:
        return node_i
    new_node = recursive_reverse(node_i.next)
    node_i.next.next = node_i #figuring out this part tripped me up the most
    node_i.next = None
    return new_node


def stack_reverse(c):
    temp = linked_list()
    for i in range(c.size()):
        temp.push(c.pop())
    return temp


class UnitTests(unittest.TestCase):
    def testReverseIterative(self):
        link = linked_list()
        n = Node(3,None)
        link.push(n)
        test = Node(4, None)
        link.push(test)
        test = Node(5, None)
        link.push(test)
        test = Node(6, None)
        link.push(test)
        self.assertEqual(link.size(),4)
        self.assertEqual(link.elementAt(0).value,6)
        self.assertEqual(link.elementAt(3).value,3)
        rev_link = iterative_reverse(link)
        self.assertEqual(rev_link.size(),4)
        self.assertEqual(rev_link.elementAt(0).value,3)
        self.assertEqual(rev_link.elementAt(1).value,4)
        self.assertEqual(rev_link.elementAt(2).value,5)
        self.assertEqual(rev_link.elementAt(3).value,6)

    def testReverseRecursive(self):
        link = linked_list()
        n = Node(3,None)
        link.push(n)
        test = Node(4, None)
        link.push(test)
        test = Node(5, None)
        link.push(test)
        test = Node(6, None)
        link.push(test)
        self.assertEqual(link.size(),4)
        self.assertEqual(link.elementAt(0).value,6)
        self.assertEqual(link.elementAt(3).value,3)
        rev_link = recursive_reverse(link.head)
        self.assertEqual(rev_link.value,3)
        self.assertEqual(rev_link.next.value,4)
        self.assertEqual(rev_link.next.next.value,5)
        self.assertEqual(rev_link.next.next.next.value,6)
        self.assertEqual(rev_link.next.next.next.next,None)

    def testStackRecursive(self):
        link = linked_list()
        n = Node(3,None)
        link.push(n)
        test = Node(4, None)
        link.push(test)
        test = Node(5, None)
        link.push(test)
        test = Node(6, None)
        link.push(test)
        self.assertEqual(link.size(),4)
        self.assertEqual(link.elementAt(0).value,6)
        self.assertEqual(link.elementAt(3).value,3)
        rev_link = stack_reverse(link)
        self.assertEqual(rev_link.size(),4)
        self.assertEqual(rev_link.elementAt(0).value,3)
        self.assertEqual(rev_link.elementAt(1).value,4)
        self.assertEqual(rev_link.elementAt(2).value,5)
        self.assertEqual(rev_link.elementAt(3).value,6)

if __name__ == '__main__':
    unittest.main()
