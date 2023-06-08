#!/usr/bin/python3
def magic_calculation(number1, number2):
    from magic_calculation_102 import add, sub

    if number1 < number2:
        c = add(number1, number2)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(number1, number2))
