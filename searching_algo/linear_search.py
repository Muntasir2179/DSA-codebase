
def linear_search(arr, target):
    size = len(arr)
    for i in range(size):
        if arr[i] == target:
            return i
    return -1


my_arr = [10, 2, 4, 56, 67, 90, 34, 545]
target = 4

result = linear_search(my_arr, target)
print(result)
print(my_arr.index(10))
