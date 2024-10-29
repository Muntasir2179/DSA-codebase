import sys


def print_num(num):
    if num != 0:
        print_num(num-1)
        print(num)


def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


# let's breakdown the steps of PMI
def power(base, exp):
    # base case (1)
    if exp == 1:
        return base
    
    small_task_answer = power(base, exp - 1)  # assume (2) -> Induction hypothesis

    answer = base * small_task_answer  # (3) using (2)
    return answer


def get_nth_sum(num):
    if num == 1:
        return num
    return num + get_nth_sum(num - 1)


def get_number_of_digits(number):
    if number >= 1 and number <= 9:
        return 1
    return 1 + get_number_of_digits(number // 10)


def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    
    last = fibonacci(num-1)
    second_last = fibonacci(num-2)

    return last + second_last


if __name__ == "__main__":
    # sys.setrecursionlimit(1001)
    # print(factorial(5))
    # print(power(3, 4))
    # print(get_nth_sum(10))
    # print(get_number_of_digits(910))
    print(fibonacci(4))
