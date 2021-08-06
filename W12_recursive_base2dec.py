"""
Recursively Converting a List of Digits to a Number
Write a recursive function base2dec(digits, base) that takes the list of digits in the given base and returns the corresponding base 10 number.
"""
def base2dec(digits, base):
    if len(digits) == 1:
        return digits[0]
    else:
        return digits[-1] + base * base2dec(digits[:-1], base)