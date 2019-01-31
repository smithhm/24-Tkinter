"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Haiden Smith.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    window = tkinter.Tk()
    # window.mainloop()
    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    frame1 = ttk.Frame(window, padding=30)
    frame1.grid()
    # window.mainloop()
    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    button1 = ttk.Button(frame1, text="PUT WORDS IN ME")
    # button1.grid()
    # window.mainloop()
    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    # button1['command'] = (lambda: print('Hello'))
    # window.mainloop()
    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    # button1['command'] = (lambda: todo_six(my_entry_box))
    button1.grid()

    button2 = ttk.Button(frame1, text="Button 2")
    button2.grid()
    # window.mainloop()

    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    my_entry_box2 = ttk.Entry(frame1)
    my_entry_box2.grid()

    button3 = ttk.Button(frame1, text="Button 3")
    button3['command'] = (lambda: todo_seven(my_entry_box, my_entry_box2))
    button3.grid()

    window.mainloop()
    # -------------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------


def todo_six(entry_box):
    contents = entry_box.get()
    if contents == 'ok':
        print("Hello")
    else:
        print("Goodbye")


def todo_seven(entry_box, entry_box2):
    s = entry_box.get()
    n = int(entry_box2.get())

    for k in range(n):
        print(s)


main()
