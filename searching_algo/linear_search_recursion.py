
# tail recursion
def linear_search_with_recursion(arr, n, index):
    if len(arr) == index:
        return False
    
    if arr[index] == n:
        return True
    return linear_search_with_recursion(arr, n, index+1)


if __name__ == "__main__":
    arr = [i for i in range(10000)]
    # print(linear_search_with_recursion([1, 2, 3, 4, 5, 6, 7, 8], 6, 0))
    print(linear_search_with_recursion(arr, 6, 0))
