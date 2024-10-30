

def print_all_index(arr, n, index=0):
    if index > len(arr) - 1:
        return
    
    if arr[index] == n:
        print(index)
    
    print_all_index(arr, n, index+1)


if __name__ == "__main__":
    print_all_index([2, 4, 6, 5, 6, 1, 3, 2], 2)
