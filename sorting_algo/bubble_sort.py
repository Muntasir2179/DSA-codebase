
def bubble_sort(arr):
    length = len(arr)
    for passes in range(length-1):
        for i in range(length-1-passes):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


# my_arr = [10, 2, 4, 56, 67, 90, 34, 545]
my_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(my_arr)
print(my_arr)
