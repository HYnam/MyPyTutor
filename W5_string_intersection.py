"""
                Intersecting Strings
Write a function intersection(str1, str2) which returns the intersection of str1 and str2. (Intersection means that one of the characters in str2 occurs somewhere in str1.) Each letter should be represented at most once in the output.

The letters should be in the order they appear in the first string. You should use a for loop to iterate over the first string.
"""

def intersection(str1, str2):
    out = ""
    for c in str1:
        if c in str2 and not c in out:
            out += c
    return out