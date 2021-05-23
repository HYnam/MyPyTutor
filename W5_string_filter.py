"""
                Filtering Characters from a String
Write a function filter_string(str1, str2) which returns a copy of str1 with all characters from str2 removed.

You should use a for loop to iterate over str1.
"""

def filter_string(str1, str2):
    for string in str2:
        str1 = str1.replace(string, '')
    return str1