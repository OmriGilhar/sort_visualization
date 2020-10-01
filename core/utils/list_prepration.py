import random


def create_list(number_of_elements: int, start: int, stop: int):
    return random.sample(range(start, stop), number_of_elements)

