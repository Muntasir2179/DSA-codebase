

def sum_of_array_head(arr):
    if len(arr) == 0:
        return 0
    
    return arr[0] + sum_of_array_head(arr[1:])


def sum_of_array_tail(arr, accumulator=0):
    if len(arr) == 0:
        return accumulator
    
    accumulator = accumulator + arr[0]
    return sum_of_array_tail(arr[1:], accumulator)


if __name__ == "__main__":
    print(sum_of_array_head([1, 2, 3, 4, 5]))   # more memory use
    print(sum_of_array_tail([1, 2, 3, 4, 5]))   # less memory use
