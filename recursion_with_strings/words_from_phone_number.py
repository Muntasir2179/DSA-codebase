
keys = {
    '1': '',
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
}

def return_all_words(string):
    if string == "":
        return [""]
    
    ans = []
    small_input_words = return_all_words(string[1:])
    keys_letter = keys[string[0]]

    for my_char in keys_letter:
        for word in small_input_words:
            ans.append(my_char + word)
    
    return ans



if __name__ == "__main__":
    ans = return_all_words("23")
    print(ans)
