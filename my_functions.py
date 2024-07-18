def add(number_one: int, number_two: int) -> int:
    return number_one + number_two


def divide(number_one: int, number_two: int) -> float | int:
    if number_two == 0:
        raise ValueError
    return number_one / number_two