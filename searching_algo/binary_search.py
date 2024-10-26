

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1


my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_arr, 10))
