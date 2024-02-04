def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Dzielenie przez zero nie jest dozwolone")
    return a / b


if __name__ == "__main__":
    print(add_numbers(2, 3))
    print(subtract_numbers(2, 3))
    print(multiply_numbers(2, 3))
    print(divide_numbers(2, 3))
    print(divide_numbers(2, 0))
