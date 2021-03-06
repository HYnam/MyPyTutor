"""
While Using Break
Sometimes it is convenient to be able to break out of a while loop from within the body of the while loop using the break command. This is often the case when it is more sensible to test a condition in the body that is different from the while loop condition.

A typical case is

while condition1:
    some_code
    if condition2:
       break
    more_code
If the execution gets to the if statement and condition2 is true then the while loop is exited.

This problem is a variant of the while loop problem but instead of specifying the number of numbers to be entered, the loop is terminated when the user enters the empty string (blank line).

Write a program that uses a while loop to repeatedly prompt the user for numbers and adds the numbers to a running total. When a blank line is entered, the program should print the average of all the numbers entered. You need to use a break statement to exit the while loop.

Note: This approach of exiting from a loop in the middle is generally poor programming practice. It is introduced because you will encounter it in code that you read from other sources. There are times when it is an appropriate solution, but that decision is based on design experience determining that it is a simpler solution than providing the logic to continue through half of the loop. If the body of the loop has several if conditions or several lines of code this type of break can make the logic difficult to follow and should be avoided. For assignments in this and following courses you should avoid breaking from the middle of a loop unless you are confident it is the simplest solution.
"""

entries = []

count = 0
while True:
    entry = input('Entry:')
    if not entry: # catch empty string and break the loop
        break
    entries.append(float(entry)) 

average = sum(entries)/len(entries)
print(average)

