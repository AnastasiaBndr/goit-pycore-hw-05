from typing import Callable
from decimal import Decimal


def generator_numbers(text: str):
    number_array = list(filter(lambda x: x.replace(
        '.', '', 1).isdigit() == True, text.lower().split(' ')))
    for i in number_array:
        yield float(i)


def sum_profit(text: str, generator: Callable):
    sum = 0
    for i in generator(text):
        sum += i
    return sum


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
