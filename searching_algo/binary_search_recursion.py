

def binary_search_recursion_helper(arr, n, start_idx, end_idx):
    if start_idx > end_idx:
        return False
    
    mid = start_idx + (end_idx - start_idx)//2

    if n < arr[mid]:
        return binary_search_recursion_helper(arr, n, start_idx, mid-1)
    elif n > arr[mid]:
        return binary_search_recursion_helper(arr, n, mid+1, end_idx)
    else:
        return True


def binary_search_recursion(arr, n):
    return binary_search_recursion_helper(arr, n, 0, len(arr)-1)


if __name__ == "__main__":
    arr = [i for i in range(100)]
    print(binary_search_recursion(arr, 7))
