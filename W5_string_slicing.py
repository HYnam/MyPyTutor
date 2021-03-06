"""
                            Slicing Strings
Any iterable object can be sliced. Slicing is used to extract a sub-collection of elements. For example, slicing can be used to get elements for a range of indices.

Write a function slice_from(string, start, end) which returns the characters in string from index start up to, but not including, index end. (Note that this characteristic of including the character at the start index, but not including the one at the end index, is the default slicing behavior.)

Write a function reverse_string(string) which returns the characters in string in reverse order. You must use a single slice statement to achieve this.
"""

def slice_from(string, start, end) -> str:
    string = string[start:end]
    return string;

def reverse_string(string):
    string = string[::-1] 
    return string

