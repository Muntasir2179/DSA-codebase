

def print_permutation(string, taken_sofar):
    if string == "":
        print(taken_sofar)
        return
    
    current_char = string[0]
    small_input = string[1:]

    for i in range(0, len(taken_sofar) + 1):
        print_permutation(small_input, taken_sofar[0:i] + current_char + taken_sofar[i:])
    return


def return_permutation(string):
    if string == "":
        return [""]
    
    current_char = string[0]
    small_permutations = return_permutation(string[1:])

    all_permutations = []
    for each_permute in small_permutations:
        for i in range(len(each_permute)+1):
            all_permutations.append(each_permute[:i] + current_char + each_permute[i:])
    
    return all_permutations


if __name__ == "__main__":
    # print_permutation("abc", "")
    print(return_permutation("abc"))
