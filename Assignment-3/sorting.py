
#sorting ex 1:Three Partition Sort
#Given an Array [5, 10, 5, 20, 5, 5, 10], sort them in a single pass.
#timing: 25 min
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
#start: 5:44
def sorted_merge(a, b):
    #a[:] = a[0:len(a)-len(b)] + b[:]
    #initial approach was to merge both arrays and then sort, but that does not take advantage of the fact that both arrays are already sorted

    ind_a = 0
    ind_b = 0
    while ind_a < len(a) - len(b) and ind_b < len(b):
        if a[ind_a] < b[ind_b]:
            ind_a += 1
        elif a[ind_a] > b[ind_b]:
            #shift over end of a and insert the value from b
            a[:] = a[0:ind_a] + [b[ind_b]] + a[ind_a:len(a)-1]
            ind_b += 1
        else:
            a[:] = a[0:ind_a] + [b[ind_b]] + a[ind_a:len(a)-1]
            ind_a += 1
            ind_b += 1
    return a

print(sorted_merge([1,2,4,8,0,0,0],[1,3,5]))
