"""
                    GUI Layout Example I
One important aspect of GUI design is the layout of widgets in an application.

In this problem you will lay out two buttons in a frame. Note that, although this problem uses buttons, the same layout ideas apply to any widget (including other frames).

You need to write a function create_layout that takes a frame as its only argument and adds two buttons at the left of the frame. The first (leftmost) button should have the label "Button1", and the other should have the label "Button2". The callback (command) for both buttons should be the pressed function.

There is no need to create a tk app (the root window and frame will be initialised for you).

You must use pack for layout and not grid.

The frame should appear as depicted below.



When you run your code an extra window screen should pop up showing your layout. You can extend the window to enhance the image.
"""
import tkinter as tk


def pressed():
    """
    Button callback function (command).

    You may alter what this function does if you wish, but you must not rename
    or delete it.

    """
    print("Button Pressed!")


def create_layout(frame):
    """
    Add two buttons to the frame.

    Both buttons should have the callback (command) pressed, and they should
    have the labels "Button1" and "Button2".

    The layout in the frame after running this function will be:
      +-----------------------+
      |[Button1][Button2]     |
      +-----------------------+

    Parameters:
        frame (tk.Frame): The frame to create the two buttons in.

    """
    b = tk.Button(frame, text='Button1', command=pressed)
    b.pack(side=tk.LEFT)

    c = tk.Button(frame, text='Button2', command=pressed)
    c.pack(side=tk.LEFT)