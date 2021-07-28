"""
                Updating a Dictionary
When working with lists, you probably noticed that you can change the value at a given index with a simple assignment statement. So, for example, the following code replaces the first element of lst with 42:

    lst[0] = 42
You can update the value for a given key in a dictionary in the same way. The general syntax for this is:

    d[key] = value
This is also how you insert new key/value pairs to a dictionary; if the key does not exist, it will be added.

Write a function add_to_dict(d, key_value_pairs) which adds each given key/value pair to the given dictionary. The argument key_value_pairs will be a list of tuples in the form (key, value).

The function should return a list of all of the key/value pairs which have changed (with their original values).
"""
def add_to_dict(d, key_value_pairs):
    newlist = []
    for item in key_value_pairs:

        # this handles your possible unpacking errors
        # if your list contains bad data 
        try:
            key, value = item
        except (TypeError,ValueError):
            print("Unable to unpack {} into key,value".format(item))

        # create entry into dict if needed, else gets existing
        entry = d.setdefault(key,value) 

        # if we created it or it is unchanged this won't execute
        if entry != value:
            # add to list
            newlist.append( (key, entry) )
            # change value
            d[key] = value

    return newlist
