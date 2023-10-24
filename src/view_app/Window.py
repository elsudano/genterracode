#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Object Window, this part is in charge to manage the window on the OS.

With this class we can abstract all the things regaqrding of the manipulate
the windows in the OS, the idea is works just in with one window and change
the contain while we press buttons.
"""

try:
    import Tkinter as gui_library
except ImportError:
    import tkinter as gui_library

class Window:
    """Windows Class.

    This class manage the window of the application.
    """

    __root = None  # Tipo ventana y se crea vacío.
    __height = None
    __width = None
    __title = None

    def __init__(self, title="Dummy Window", width=500, height=500):
        """Construct by default.

        Parameters
        ----------
        title : string
            Window title.
        width : int
            Width of the window.
        height : int
            Height of the window.
        """
        self.__root = gui_library.Tk()
        self.__height = height
        self.__width = width
        self.__title = title

    def _dark_style(self):
        """Dark style function.
    
        This function try to change the style of the window at Dark mode.
        """
        style = gui_library.Style()
        style.configure("TFrame", background="black")
        style.configure("TButton", background="gray")

    def init_ui(self):
        """Window Initialization.

        In order to create a window, this functon is public because is possible call it
        from anywhere on the application, the idea is put the default values in the window
        and then change the values if is necessary.
        """
        # Set the window in the center of the screen
        x = (self.__root.winfo_screenwidth() // 2) - (self.__width // 2)
        y = (self.__root.winfo_screenheight() // 2) - (self.__height // 2)
        # Set the window size
        self.__root.geometry('{}x{}+{}+{}'.format(self.__width, self.__height, x, y))
        # Set title
        self.__root.title(self.__title)
        # Set with is the minimun size
        self.__root.minsize(width=self.__width, height=self.__height)
        # Set the columns and rows that the window will have
        # Set a frame to occupy the whole window
        self.__root.rowconfigure(0, weight=1)
        self.__root.columnconfigure(0, weight=1)

    def size(self, width, height):
        """In order to change the window size we can use this method.

        Parameters
        ----------
        width : int
            Width of the window.
        height : int
            Height of the window.
        """
        self.__width = width
        self.__height = height

    def change_state_size(self, state):
        """Enable or disable the option regarding change the window size.

        Parameters
        ----------
        state : boolean
            set true change the size or false to maintain the size.
        """
        self.__root.resizable(width=state, height=state)
        self.init_ui()

    def set_title(self, t):
        """Set the title of the window.

        Parameters
        ----------
        t : string
            String with a title of the window.
        """
        self.__title = t
        self.init_ui()

    def get(self):
        """Give the root propierty of the window."""
        return self.__root

    def get_height (self):
        """Give the height propierty of the window"""
        return self.__height

    def get_width (self):
        """Give the width propierty of the window"""
        return self.__width

    def start(self):
        """Start the view.

        That means, that we can start to show the window in order to run the application.
        """
        self.__root.mainloop()

    def stop(self):
        """Stop the application.

        With that we can stop the view and the application as well.
        """
        self.__root.quit()
