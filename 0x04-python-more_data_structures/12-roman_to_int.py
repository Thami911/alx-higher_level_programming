#!/usr/bin/python3
def roman_to_int(r_string: str):
    if r_string is None or type(r_string) != str:
        return 0
    my_data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [my_data[x] for x in r_string] + [0]
    rep = 0

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            rep += numbers[i]
        else:
            rep -= numbers[i]

    return rep
