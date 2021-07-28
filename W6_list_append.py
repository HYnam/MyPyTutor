"""
                Transforming a List
One typical kind of list processing is to transform the elements of a list, producing a copy of the list but with the elements transformed.

Write a function definition of add_sizes using a for loop that takes a list of strings, say strings, and returns a list of pairs consisting of the elements of strings together with their lengths.
"""
def add_sizes(strings):
    """
    Return the list of pairs consisting of the elements of strings together
    with their sizes.

    Parameters:
        list<str>: a list a strings

    Return:
        list<tuple<str, int>>: a list of strings and their corresponding 
        lengths
        
    """
    c = []
    for i in strings:
        c.append((i, len(i)))
    return c