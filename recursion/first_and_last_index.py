
def get_first_index(arr, n):
    if len(arr) == 0:
        return -1
    
    if arr[0] == n:
        return 0
    
    ans_from_recursion = get_first_index(arr[1:], n)

    if ans_from_recursion == -1:
        return ans_from_recursion
    else:
        return ans_from_recursion + 1
    

def get_last_index(arr, n):
    if len(arr) == 0:
        return -1
    
    ans_from_recursion = get_last_index(arr[1:], n)

    if ans_from_recursion != -1:
        return ans_from_recursion + 1
    else:
        if arr[0] == n:
            return 0
        else:
            return -1
    


if __name__ == "__main__":
    # print(get_first_index([2, 4, 6, 5, 6, 1, 3, 2], 1))
    print(get_last_index([2, 4, 6, 5, 6, 1, 3, 2], 2))
