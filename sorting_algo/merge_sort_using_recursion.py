
def merge(arr, start, mid, end):
    i = start     # start index for left array
    j = mid + 1   # start index for right array
    ans = []

    # adding each element from the argument array into answer array in a sorting manner
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            ans.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            ans.append(arr[j])
            j += 1
        elif arr[i] == arr[j]:
            ans.append(arr[i])
            ans.append(arr[j])
            i += 1
            j += 1
    
    # adding rest of the element of the argument array into answer array if any left
    while i <= mid:
        ans.append(arr[i])
        i += 1
    while j <= end:
        ans.append(arr[j])
        j += 1

    start_of_my_ans = 0
    start_of_my_list = start

    # copying the answer array into the main argument array
    while start_of_my_list <= end:
        arr[start_of_my_list] = ans[start_of_my_ans]
        start_of_my_list += 1
        start_of_my_ans += 1
    
    return


def merge_sort_helper(arr, start, end):
    if start >= end:
        return
    
    mid = start + (end - start) // 2

    merge_sort_helper(arr, start, mid)   # calling merge sort on left half
    merge_sort_helper(arr, mid+1, end)   # calling merge sort on right half

    # when left and right part of the array is sorted individually, we are merging them in sorted manner
    merge(arr, start, mid, end)


def merge_sort(arr):
    return merge_sort_helper(arr, 0, len(arr)-1)


if __name__ == "__main__":
    arr = [4, 5, 6, 1, 2, 3]
    merge_sort(arr)
    print(arr)
