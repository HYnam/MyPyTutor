"""
                    Using Range
The built-in function range returns an iterable sequence of numbers.

Write a function sum_range(start, end) which uses range to return the sum of the numbers from start up to, but not including, end. (Including start but excluding end is the default behaviour of range.)

Write a function sum_evens(start, end) which does the same thing, but which only includes even numbers. You should also use range.
"""
def sum_range(start, end):
    x = range(start, end)
    count = 0
    for n in x:
        count += n
    return count
        
def sum_evens(start, end):
    count = 0
    for i in range(start, end, 1):
        if(i % 2 == 0):
            count += i
    return count