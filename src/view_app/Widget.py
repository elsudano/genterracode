#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Create widgets in the easy way.

We can generate components in order to add it in the view.
"""

try:
    from Tkinter import ttk
except ImportError:
    from tkinter import ttk

class Widgets:
    """Class Widgets."""

    __button = None
    __checkbutton = None
    __frame = None
    # entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton,
    # scale, Scrollbar, Combobox, Notebook, Progressbar, Separator, Sizegrip,
    # treeview

    def __init__(self):
        """Construct by default."""
        self.__checkbutton = None

    def create_button(self, parent, text, callback):
        """Add a button in the window.

        We can create a button and add it in the window just calling the function.
        """
        button = ttk.Button(parent, text=text, command=callback)
        button.grid(row=6, column=6)

    def Frame(self, parent):
        """Change the frame."""
        self.__frame = ttk.Frame(parent, padding="3 3 12 12")
