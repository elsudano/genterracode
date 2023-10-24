#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""View of the application.

This is the root part of our view, we can use this file
like a storage where we need put all our libraries for the GUI.
"""
try:
    from Tkinter import Menu as menu
    from Tkinter import ttk as ttk
    from Tkinter import tkFileDialog as filediag
    from Tkinter import tkMessageBox as msgbox
    from Tkinter import Text as text
    from Tkinter import constants as constants
    from Tkinter import IntVar
    from Tkinter import BooleanVar
except ImportError:
    # for python 3.x
    from tkinter import Menu as menu
    from tkinter import ttk as ttk
    from tkinter import messagebox as msgbox
    from tkinter import filedialog as filediag
    from tkinter import Text as text
    from tkinter import constants as constants
    from tkinter import IntVar
    from tkinter import BooleanVar

# para crear clases con padres e hijos
from abc import ABC, abstractmethod

class View(ABC):
    """View class.
    
    This is the root class to contruct the different views that
    we will have in the application
    """

    _window = None
    _controller = None
    _principal_frame = None
    _menu_bar = None
    _menus = None

    def __init__(self, window, controller):
        """Construct by default.

        Parameters
        ----------
        window : Window
            This the window where we can fill the view.
        """
        # With that we can initialize the super class ABC
        super(View, self).__init__()
        self._window = window
        self._controller = controller
        self._menu_bar = menu(self._window.get())
        self._menus = list()
        self._window.get().config(menu=self._menu_bar)

    @abstractmethod
    def _init_view(self):
        pass

    def _add_menu(self, name):
        """Add a menu in the menu bar."""
        menu_aux = menu(self._menu_bar)
        menu_aux.config(title=name)
        # FIXME: arreglar la inclusión de posicionamiento del menú
        # si queremos cambiar para que se pueda añadir un menu en la posicón
        # que queremos basta con poner un indice en los parametros de la
        # función y cambiar el indice por el len de la siguiente linea
        self._menus.insert(len(self._menus), menu_aux)

    def _add_item_menu(self, parent, name, command):
        """Add an option in one menu."""
        for menu in self._menus:
            if menu.cget('title') == parent:
                menu.add_command(label=name, command=command)
                # FIXME: arreglar la inclusión de posicionamiento del item del menú
                # menu.insert_command(0, label=name, command=command)
                # si queremos cambiar para que se pueda añadir una opción de menu
                # en la posicón que queremos basta con poner un indice en los
                # parámetros de la función y cambiar el indice de la función anterior
                # por el que se pasa por parámetros.

    def _add_menu_separator(self, name):
        """Add a separator in a menu."""
        for menu in self._menus:
            if menu.cget('title') == name:
                menu.add_separator()

    def _menu_bar_by_default(self):
        """Method to add the default menu bar in the view.
        
        With this method is ossible add the menu bar on our application
        always in the same order, and then add the new items with the 
        specific methods that we have in the class."""
        self._add_menu("Archivo")
        self._add_item_menu("Archivo", "Nuevo", self._controller.menu_item_new)
        self._add_item_menu("Archivo", "Abrir", self._controller.menu_item_open)
        self._add_item_menu("Archivo", "Guardar", self._controller.menu_item_save)
        self._add_menu_separator("Archivo")
        self._add_item_menu("Archivo", "Salir", self._controller.menu_item_exit)
        self._add_menu("Editar")
        self._add_item_menu("Editar", "Cortar", self._controller.menu_item_cut)
        self._add_item_menu("Editar", "Copiar", self._controller.menu_item_copy)
        self._add_item_menu("Editar", "Pegar", self._controller.menu_item_paste)
        self._add_menu("Ver")
        self._add_item_menu("Ver", "Barra de Herramientas", self._controller.menu_item_show_tools_bar)
        self._add_item_menu("Ver", "Barra de Estado", self._controller.menu_item_show_status_bar)
        self._add_menu("Herramientas")
        self._add_item_menu("Herramientas", "Utilidades", self._controller.menu_item_other)

    def _change_size(self, width, height):
        self._window.size(width,height)
        self._window.init_ui()

    def _default_config(self):
        """Initialize by default our view.
        
        With this method we can set all the common items in all the views
        in order to maintain the aspect that we want in our application.
        """
        # Crating the frame
        self._principal_frame = ttk.Frame(self._window.get(), padding="3 3 12 12")
        # The frame is in the 0,0 position in order to put in the center of the screen
        self._principal_frame.grid(column=0, row=0, sticky='NESW')
        # how much columns have the frame
        self._principal_frame.columnconfigure(0, weight=1)
        # how much rows have the frame 
        self._principal_frame.rowconfigure(0, weight=1)
        if self.__class__.__name__ == "MainView":
            # Creating the exit button in the frame
            self.b_exit = ttk.Button(self._principal_frame, text="Exit")
            # Setting the position of the button in 1,12
            self.b_exit.grid(column=1, columnspan=12, row=12, sticky='SE')
            # Setting which command we run when we press the button
            self.b_exit.bind("<Button>", self._controller.exit)
        else:
            # Creating the back button in the frame
            self.b_back = ttk.Button(self._principal_frame, text="Back")
            # Setting the position of the button in 1,12
            self.b_back.grid(column=1, columnspan=12, row=12, sticky='SE')
            # Setting which command we run when we press the button
            self.b_back.bind("<Button>", self._controller.back)

    def init_view(self):
        """Initialize the view in the Window.

        With this method we can start to show the view in the window.
        """
        self._menu_bar_by_default() # we add the menu bar by default
        self._init_view() # we initilize the view and then we add the extra menus
        for menu in self._menus:
            self._menu_bar.add_cascade(label=menu.cget('title'), menu=menu)

    def __delete__(self, instance):
        """We can destroy the view with this method."""
        self._principal_frame.destroy()
