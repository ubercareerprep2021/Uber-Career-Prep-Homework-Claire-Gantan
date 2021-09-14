#searching exercise 1: find minimum in a rotated and sorted array
#Input: {4, 5, 1, 2, 3}
#Output: {1}
#timing: 25 min
#thought process: since the array is sorted in some sense we can attempt to use a binary search
def find_min(arr):
    return find_min_helper(arr, 0, len(arr))

def find_min_helper(arr, start, end):
    midpoint = int((end-start)/2)+start
    # print(arr[start:end])
    # print(arr[midpoint])
    if end-start == 1:
        return arr[start]
    elif end-start == 2:
        return min(arr[start], arr[start+1])
    elif arr[midpoint] > arr[midpoint -1] and arr[midpoint] < arr[midpoint+1]:
        # print("min is in first half")
        return find_min_helper(arr,start, midpoint)
    else:
        # print("min is in second half")
        return find_min_helper(arr,midpoint,end)

print("output should be all 1s for the minimum")
print(find_min([1,2]))
print(find_min([4,5,1,2,3]))
print(find_min([1,2,3,4,5]))
print(find_min([6,1,2,3,4,5]))

#searching exercise 2: find element in a rotated and sorted array
#assuming we return the index, else return -1
# input: [4,5,1,2,3], 2
#output: 3
#timing: 8:33-
#thought process: since the array is sorted in some sense we can attempt to use a binary search
def find_element(arr, val):
    return find_element_helper(arr, 0, len(arr), val)

def find_element_helper(arr, start, end, val):
    midpoint = int((end-start)/2)+start
    # print(arr[start:end])
    # print(arr[midpoint])
    if end-start == 1:
        if arr[start] == val:
            return start
        return -1
    elif end-start == 2:
        return start if arr[start] == val else (start + 1 if arr[start+1] == val else -1)
    elif arr[midpoint] == val:
        return midpoint
    elif arr[midpoint+1] < val:
        # print("min is in first half")
        return find_element_helper(arr,start, midpoint, val)
    else:
        # print("min is in second half")
        return find_element_helper(arr,midpoint,end, val)
print("finding elements, should be 0 -1 -1 0 1 3 1")
print(find_element([1],1))
print(find_element([1],0))
print(find_element([1,2],0))
print(find_element([1,2],1))
print(find_element([1,2],2))
print(find_element([4,5,1,2,3],2))
print(find_element([4,5,1,2,3],5))
