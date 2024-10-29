
def fact_head(number):
    if number == 0:
        return 1
    small_ans = fact_head(number-1)
    final_ans = number * small_ans
    return final_ans


def fact_tail_wrong(number):
    if number == 1:
        return 1
    return number * fact_tail_wrong(number-1)


def fact_tail(number, accumulator=1):
    if number == 0:
        return accumulator
    accumulator = accumulator * number
    return fact_tail(number-1, accumulator)


# head recursion
def print_1_to_n(n):
    if n <= 0:
        return
    
    print_1_to_n(n-1)
    print(n)


# tail recursion
def print_n_to_1(n):
    if n <= 0:
        return
    
    print(n)
    print_n_to_1(n-1)


def sum_of_digits(number):
    if number >= 0 and number <= 9:
        return number
    return (number % 10) + sum_of_digits(number//10)


if __name__ == "__main__":
    # print(fact_tail(4))
    # print_1_to_n(5)
    # print_n_to_1(5)
    print(sum_of_digits(12345))
