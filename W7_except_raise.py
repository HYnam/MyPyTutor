"""
            Raising an Exception
In the previous problem, you used a try/except statement to catch an exception. This problem deals with the opposite situation: raising an exception in the first place.

One common situation in which you will want to raise an exception is where you need to indicate that some precondition that your code relies upon has not been met. (You may also see the assert statement used for this purpose, but we won’t cover that here.)

Write a function validate_input(string) which takes a command string in the format 'command arg1 arg2' and returns the pair ('command', [arg1, arg2]), where arg1 and arg2 have been converted to floats. If the command is not one of 'add', 'sub', 'mul', or 'div', it must raise InvalidCommand. If the arguments cannot be converted to floats, it must raise InvalidCommand.
"""
class InvalidCommand(Exception):
    pass


def validate_input(string):
    """
    If string is a valid command, return its name and arguments.
    If string is not a valid command, raise InvalidCommand

    Valid commands:
      add x y
      sub x y
      mul x y
      div x y

    Parameters:
        string(str): a valid command (see above)

    Return:
        tuple<str, list<float>>: the command and its corresponding arguements

    Precondition:
        Arguments x and y must be convertable to float.
        
    """
    # your code here
    lst = string.split(' ')
    commands = ['add', 'sub', 'mul', 'div']
    if lst[0] not in commands:
        raise InvalidCommand()
    if len(lst) != 3:
        raise InvalidCommand()
    try:
        arg1 = float(lst[1])
        arg2 = float(lst[2])
        return(lst[0], [arg1, arg2])
    except ValueError:
        raise InvalidCommand()