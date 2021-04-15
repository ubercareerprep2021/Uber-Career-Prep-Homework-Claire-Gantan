import unittest

class Stack:
    def __init__(self):
        self.list = []

    def push(self, num):
        self.list = [num] + self.list[:]

    def pop(self):
        if self.isEmpty():
            return None
        value = self.list[0]
        self.list = self.list[1:]
        return value

    def top(self):
        if self.isEmpty():
            return None
        return self.list[0]

    def isEmpty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

# made this into an actual unit test below
#example test code given
# myStack = Stack()
# myStack.push(42)
# print('Top of stack: ', myStack.top())
# # prints “Top of stack: 42”
# print('Size of stack: ', myStack.size())
# # prints “Size of stack: 1”
# popped_value = myStack.pop()
# print('Popped value: ', popped_value)
# # prints “Popped value: 42”
# print('Size of stack: ', myStack.size())
# # prints “Size of stack: 0”
#
# # need to also check what happens if you have more items than you push
# print('Top of stack: ', myStack.top())
# print('Popped stack: ', myStack.pop())


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue = self.queue[:]+[val]

    def dequeue(self):
        if self.isEmpty():
            return None
        item = self.queue[0]
        self.queue = self.queue[1:]
        return item

    def rear(self):
        if self.isEmpty():
            return None
        return self.queue[-1]

    def front(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.size() == 0

# made this into an actual unit test below
# print()
# myQueue = Queue()
# myQueue.enqueue(1)
# myQueue.enqueue(2)
# myQueue.enqueue(3)
# print('Size of queue: ', myQueue.size())
# # prints “Size of queue: 3”
# print ('Front of queue: ', myQueue.front())
# # prints “Front of queue: 1”
# print('Rear of queue: ', myQueue.rear())
# # prints “Rear of queue: 3”
# dequeuedItem = myQueue.dequeue()
# print('Dequeue item: ', dequeuedItem)
# # prints “Dequeued item: 1”

# made this into an actual unit test below
# print('string queue')
# myQueue = Queue()
# myQueue.enqueue('pizza')
# myQueue.enqueue('burrito')
# print('Size of queue: ', myQueue.size())
# print('Front of queue: ', myQueue.front())
# print('Rear of queue: ', myQueue.rear())
# dequeuedItem = myQueue.dequeue()
# dequeuedItem = myQueue.dequeue()
# print('Second dequeued item: ', dequeuedItem)
# print ('Front after dequeing everything: ', myQueue.front())


class UnitTests(unittest.TestCase):
    def testQueueSize(self):
        myQueue = Queue()
        self.assertEqual(myQueue.size(),0)
        self.assertTrue(myQueue.isEmpty())
        myQueue.enqueue(1)
        myQueue.enqueue(2)
        myQueue.enqueue(3)
        self.assertEqual(myQueue.size(),3)

    def testQueueQueing(self):
        myQueue = Queue()
        myQueue.enqueue(4)
        myQueue.enqueue(2)
        myQueue.enqueue(3)
        self.assertEqual(myQueue.size(),3)
        self.assertEqual(myQueue.front(),4)
        self.assertEqual(myQueue.rear(),3)
        self.assertEqual(myQueue.dequeue(),4)

    def testStringQueue(self):
        myQueue = Queue()
        myQueue.enqueue('pizza')
        myQueue.enqueue('burrito')
        self.assertEqual(myQueue.size(),2)
        self.assertEqual(myQueue.front(),'pizza')
        self.assertEqual(myQueue.rear(),'burrito')
        self.assertEqual(myQueue.dequeue(),'pizza')
        self.assertEqual(myQueue.dequeue(),'burrito')
        self.assertEqual(myQueue.dequeue(),None)

    def testStackBasic(self):
        myStack = Stack()
        myStack.push(42)
        self.assertEqual(myStack.top(),42)
        self.assertEqual(myStack.size(),1)
        self.assertEqual(myStack.pop(),42)
        self.assertEqual(myStack.size(),0)

    def testStackPopTooMuch(self):
        myStack = Stack()
        myStack.push('abc')
        self.assertEqual(myStack.top(),'abc')
        self.assertEqual(myStack.size(),1)
        self.assertEqual(myStack.pop(),'abc')
        self.assertEqual(myStack.pop(),None)

#not sure what this does or if it is just syntax??
if __name__ == '__main__':
    unittest.main()

#started 11:40am - 11:55 for stack
#11:55-12:08 for queue
#afterwards, looked up unit test stuff! writing unit tests = 20 min

#TOTAL = 28 min
#reflection: using Python instead of Java definitely made everything faster and easier for me, although I could have thought through it more before coding
