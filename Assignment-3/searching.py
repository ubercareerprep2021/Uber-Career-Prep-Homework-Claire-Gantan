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
