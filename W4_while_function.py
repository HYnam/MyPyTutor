"""
Writing a Function Using While
    Write a function div_3_5(start, end) that computes the number of integers from start up to, but not including end that are divisible by 3 or 5 using a while loop.

Examples:
div_3_5(7, 27) evaluates to 9 ( numbers divisible by 3 or 5 in that range: 9,10,12,15,18,20,21,24,25)
"""

def div_3_5(start, end):
    """ Return the integers that are divisible by 3 or 5
    include start but not end number
    
    Parameters:
        start(int) - start value, included
        end(int) - end value, not included
        
    Return:
        int: Numbers that are divisible by 3 or 5, including start value but not end value
    """
    numbers_3_5 = []
    while start < end:
        if start % 3 == 0 or start % 5 == 0:
            numbers_3_5.append(start)
        start += 1
    return len(numbers_3_5)