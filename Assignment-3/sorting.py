
#sorting ex 1:Three Partition Sort
#Given an Array [5, 10, 5, 20, 5, 5, 10], sort them in a single pass.
#timing: 5:12
#was recommended to use the three_partition_sort
def three_partition_sort(arr, pivot):
    pivot_val = arr[pivot]
    swap_index = 0
    #forward sort
    for i in range(len(arr)):
        if arr[i] < pivot_val:
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            swap_index += 1
    #backwards sort
    swap_index = len(arr) - 1
    for i in range(1, len(arr) + 1):
        if arr[len(arr)-i] > pivot_val:
            arr[len(arr)-i], arr[swap_index] = arr[swap_index], arr[len(arr)-i]
    return arr

print(three_partition_sort([5, 10, 5, 20, 5, 5, 10], 1))
#Sorting Exercise 2: External Sort
#Given a large array containing a million entries, sort them by loading only 100 entries at a time in memory.


#Sorting Exercise 3: Sorted Merge
#You are given two sorted arrays, A and B, where A has a large enough buffer at the
#end to hold B. Write a method to merge B into A in sorted order in one pass and using O(1) space.
#def sorted_merge(a, b):
