"""
            Recursion - Extracting Digits
Write a recursive function getdigits(n) that returns the list of digits in the positive integer n.
"""
def getdigits(n):
    if n<10:
        return [n]
    else:
        return getdigits(n//10)+[n%10]