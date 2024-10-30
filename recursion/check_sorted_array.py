
# head recursion
def check_if_sorted_head(arr):
    # if list has only one or no element then it will be already sorted
    if len(arr) == 0 or len(arr) == 1:
        return True

    # recursive call
    ans = check_if_sorted_head(arr[1:])

    # our work
    if arr[0] <= arr[1]:
        return ans
    else:
        return False


# tail recursion
def check_if_sorted_tail(arr):
    # if list has only one or no element then it will be already sorted
    if len(arr) == 0 or len(arr) == 1:
        return True

    # our work
    if arr[0] > arr[1]:
        return False
    return check_if_sorted_tail(arr[1:])



if __name__ == "__main__":
    small_arr = [1, 1, 2, 3, 4, 4, 5]
    # big_arr = [i for i in range(10000, 1, -1)]
    print(check_if_sorted_tail(small_arr))   # as it is using tail recursion, this execution will succeed and will give an answer

    try:
        print(check_if_sorted_head(small_arr))   # as the array is huge and it uses head recursion, this execution going to fail
    except Exception as e:
        print(e)
