

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        current_min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[current_min_idx]:
                current_min_idx = j
        
        if current_min_idx != i:
            arr[i], arr[current_min_idx] = arr[current_min_idx], arr[i] 


my_arr = [100, 12, 25, 11, 34, 90, 22]
# my_arr = [11, 12, 22, 25, 34, 90, 100]

selection_sort(my_arr)
print(my_arr)
