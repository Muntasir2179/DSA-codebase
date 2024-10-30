
def update_indices_of_element_in_provided_list(arr, n, index, ans_list:list):
    if index > len(arr) - 1:
        return
    
    if arr[index] == n:
        ans_list.append(index)

    update_indices_of_element_in_provided_list(arr, n, index+1, ans_list)
    

def update_indices_of_element_and_return_list(arr, n, index):
    if index > len(arr) - 1:
        return []
    
    small_list = update_indices_of_element_and_return_list(arr, n, index+1)

    if arr[index] == n:
        small_list.insert(0, index)
        # small_list = [index] + small_list   # alternative way
    
    return small_list


if __name__ == "__main__":
    ans_list = []
    update_indices_of_element_in_provided_list([2, 4, 6, 5, 2, 6, 1, 3, 2], 2, 0, ans_list)
    print(ans_list)
    print(update_indices_of_element_and_return_list([2, 4, 6, 5, 2, 6, 1, 3, 2], 2, 0))
