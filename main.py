"""This Python file tests my ability to do static analysis."""
from line_profiler import profile


@profile
def expensive_op(n):
    """This function calculates the expensive operation of an integer n."""
    # total = 0
    # for i in range(1000):
    #     total += i * n
    # return total

    # (999 * 1000) / 2 = 499500
    return n * 499500


@profile
def slow_func(lst):
    """This function is a slow function."""
    # result = []
    # for i in range(len(lst)):
    #     result.append(expensive_op(i))
    # return result

    return [i * 49950 for i in range(len(lst))]


@profile
def main():
    """This is the main function."""
    numbers = list(range(1000))
    output = slow_func(numbers)
    print(output)
    print("Done")


if __name__ == "__main__":
    main()
