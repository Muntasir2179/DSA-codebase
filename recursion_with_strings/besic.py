
def remove_character(string, char):
    if string == "":
        return string
    
    small_answer = remove_character(string[1:], char)

    if string[0] == char:
        return small_answer
    else:
        return string[0] + small_answer


def is_palindrome(string):
    if string == "":
        return True
    
    if string[0] != string[-1]:
        return False
    else:
        return is_palindrome(string[1:-1])   # slicing creates a new memory in the ram
    

# in this case we are not using slicing of string,
# we are just updating the start and end indices for comparing characters
def is_palindrome_better(string, start, end):
    if start >= end:
        return True
    
    if string[start] != string[end]:
        return False
    else:
        return is_palindrome_better(string, start+1, end-1)


if __name__ == "__main__":
    string = "nitin"
    # print(remove_character(string, "n"))
    print(is_palindrome(string))
    print(is_palindrome_better(string, 0, len(string)-1))

