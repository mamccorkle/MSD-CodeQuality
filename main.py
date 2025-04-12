"""This Python file tests my ability to do static analysis."""


def expensive_op(n):
    """This function calculates the expensive operation of an integer n."""
    total = 0
    for i in range(1000):
        total += i * n
    return total


def slow_func(lst):
    """This function is a slow function."""
    result = []
    for i in range(len(lst)):
        result.append(expensive_op(i))
    return result


def unused_function():
    """This is an unused function."""
    x = 10
    y = 20
    z = x + y
    return z


def main():
    """This is the main function."""
    numbers = list(range(1000))
    output = slow_func(numbers)
    print(output)
    print("Done")


if __name__ == "__main__":
    main()
