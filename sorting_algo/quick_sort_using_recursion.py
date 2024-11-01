
def partition(arr, start, end):
    pivot = arr[end]
    i = pivot_index = start

    # loop to fine the pivot index
    while i < end:
        if arr[i] < pivot:
            pivot_index += 1
        i += 1

    # swapping for moving the pivot element to the right position which is the pivot index
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    
    s = start
    e = end

    # now make sure that everything smaller then pivot to left and greater to right
    while s < pivot_index and e > pivot_index:
        if arr[s] < pivot:
            s += 1
        elif arr[e] >= pivot:
            e -= 1
        else:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    
    return pivot_index


def quick_sort(arr, start, end):
    if start >= end:   # base case
        return
    
    # get the pivot index
    pivot_index = partition(arr, start, end)

    quick_sort(arr, start, pivot_index-1)   # calling merge sort on left part
    quick_sort(arr, pivot_index+1, end)     # calling merge sort on right part


if __name__ == "__main__":
    arr = [5, 3, 6, 8, 2, 1, 8, 7]
    quick_sort(arr, 0, len(arr)-1)
    # print(partition(arr, 0, len(arr)-1))
    print(arr)
