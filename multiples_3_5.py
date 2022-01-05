
def is_multiple(number: int, factor: int) -> bool:
    rest = number % factor
    return rest == 0


def sum_multiples_under_number(limit: int) -> int:
    sum_multiples = 0
    for num in range(1, limit):
        if is_multiple(num, 3):
            sum_multiples = sum_multiples + num
        elif is_multiple(num, 5):
            sum_multiples = sum_multiples + num
    return sum_multiples


print(sum_multiples_under_number(1000))
