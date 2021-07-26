
#sorting ex 1:Three Partition Sort
#Given an Array [5, 10, 5, 20, 5, 5, 10], sort them in a single pass.
#timing: 11:48
def three_partition_sort(arr):
    #are we guaranteed that they are in the same order?
    #if so:
    arr[1], arr[4] = arr[4], arr[1] # arr = [5, 5, 5, 20, 10, 5, 10]
    arr[3], arr[5] = arr[5], arr[3] # arr = [5, 5, 5, 5, 10, 20, 10]
    arr[3], arr[5] = arr[5], arr[3] # arr = [5, 5, 5, 5, 10, 20, 10]
    arr[5], arr[6] = arr[6], arr[5] # arr = [5, 5, 5, 5, 10, 10, 20]
    return arr

#Sorting Exercise 2: External Sort
#Given a large array containing a million entries, sort them by loading only 100 entries at a time in memory.


#Sorting Exercise 3: Sorted Merge
#You are given two sorted arrays, A and B, where A has a large enough buffer at the
#end to hold B. Write a method to merge B into A in sorted order in one pass and using O(1) space.
def sorted_merge(a, b):
