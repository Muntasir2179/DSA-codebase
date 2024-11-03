
def get_subsequences(string):
    if string == "":
        return [""]
    
    small_ans = get_subsequences(string[1:])   # calculating sub sequences for string after current character
    current_char = string[0]
    ans = []
    ans.extend(small_ans)   # appending all the elements from small answer into the answer

    # multiplying current character with the returned small answer
    for each_permutation in small_ans:
        ans.append(current_char + each_permutation)
    return ans


def print_subsequence(string, taken_sofar):
    if string == "":
        print(taken_sofar)
        return
    
    current_char = string[0]
    small_input = string[1:]

    print_subsequence(small_input, taken_sofar + current_char)  # taken
    print_subsequence(small_input, taken_sofar)  # not taken

    return


if __name__ == "__main__":
    string = "abc"
    # ans = get_subsequences(string)
    # print(ans)
    print_subsequence(string, "")

