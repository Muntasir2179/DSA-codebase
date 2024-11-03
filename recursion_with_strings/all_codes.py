

def get_char(value):
    if value <= 0 or value > 26:
        return ""
    return chr(97 + value - 1)


def return_all_codes(string):
    if string == "":   # base case
        return [""]
    
    if len(string) == 1:  # base case for single digit
        return [get_char(int(string))]
    
    single_digit = int(string[0:1])
    double_digit = int(string[0:2])
    ans = []

    ans_without_first_digit = return_all_codes(string[1:])
    for each_ans in ans_without_first_digit:
        ans.append(get_char(int(single_digit)) + each_ans)
    
    if double_digit >= 10 and double_digit <= 26:
        ans_without_first_two_digit = return_all_codes(string[2:])
        for each_ans in ans_without_first_two_digit:
            ans.append(get_char(int(double_digit)) + each_ans)
    
    return ans


if __name__ == "__main__":
    ans = return_all_codes("1123")
    print(ans)
