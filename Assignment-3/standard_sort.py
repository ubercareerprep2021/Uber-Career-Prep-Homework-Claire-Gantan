import unittest
#standard sorting algorithms 1
#timing: 1:02
def insertion_sort(arr, compare):
    for i in range(1, len(arr)):
        for n in range(0, i-1):
            #find where to put arr[i], shift up everything else
            i += 1
    return []

def bubble_sort(arr, compare):
    #recursive idea: repeat until there is a pass with no swaps (everything is in order)
    # swaps = 0
    # for i in range(1, len(arr)):
    #     if not compare(arr[i-1], arr[i]):
    #         arr[i-1], arr[i] = arr[i], arr[i-1]
    #         swaps += 1
    # if swaps > 0:
    #     bubble_sort(arr, compare)
    # return arr

    #following example on the doc
    for i in range(len(arr)-1):
        for n in range(len(arr)-i-1):
            if not compare(arr[n], arr[n+1]):
                arr[n], arr[n+1] = arr[n+1], arr[n]
    return arr

def selection_sort(arr, compare):
    for i in range(len(arr)):
        small_index = i
        for n in range(i, len(arr)):
            if not compare(arr[small_index], arr[n]):
                small_index = n
        #swap value at i with value at small_index
        arr[small_index], arr[i] = arr[i], arr[small_index]
    return arr

def ascending_compare(a, b):
    #returns true if b >= a, checks if a < b
    return a <= b

def descending_compare(a, b):
    return a > b

class UnitTests(unittest.TestCase):
    def test_bubble(self):
        self.assertEqual(bubble_sort([7, 4, 5, 2], ascending_compare),[2,4,5,7])
        self.assertEqual(bubble_sort([7, 7, 5, 2, 0], ascending_compare),[0,2,5,7,7])
        self.assertEqual(bubble_sort([7, 4, 5, 2], descending_compare),[7,5,4,2])
        self.assertEqual(bubble_sort([7, 7, 5, 2, 0], descending_compare),[7,7,5,2,0])

    def test_selection(self):
        self.assertEqual(selection_sort([7, 4, 5, 2], ascending_compare),[2,4,5,7])
        self.assertEqual(selection_sort([7, 7, 5, 2, 0], ascending_compare),[0,2,5,7,7])
        self.assertEqual(selection_sort([7, 4, 5, 2], descending_compare),[7,5,4,2])
        self.assertEqual(selection_sort([7, 7, 5, 2, 0], descending_compare),[7,7,5,2,0])

    def test_insertion(self):
        self.assertEqual(insertion_sort([7, 4, 5, 2], ascending_compare),[2,4,5,7])
        self.assertEqual(insertion_sort([7, 7, 5, 2, 0], ascending_compare),[0,2,5,7,7])
        self.assertEqual(insertion_sort([7, 4, 5, 2], descending_compare),[7,5,4,2])
        self.assertEqual(insertion_sort([7, 7, 5, 2, 0], descending_compare),[7,7,5,2,0])


if __name__ == '__main__':
    unittest.main()
