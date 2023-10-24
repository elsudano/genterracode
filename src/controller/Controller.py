#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Controlador principal del programa.

This is the root part of our controllers, we can use this file
like a storage where we need put all our libraries.
"""

# The principal class about herancy
from abc import ABC, abstractmethod
# class to manage the file path that we will need
from pathlib import Path

class Controller(ABC):
    """Controller class."""

    _window = None
    _model = None
    _view = None

    def __init__(self, window, model):
        """Construct by default."""
        self._window = window
        self._model = model

    @abstractmethod
    def back(self, event):
        pass

    def set_view(self, view):
        """Asignar la vista del controlador.

        Con esto asignamos la vista al controlador para poder utilizarla
        """
        self._view = view

    def menu_item_new(self):
        """Crear un nuevo Objeto.

        Realiza todas las operaciones para crear un nuevo Objeto.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Archivo/Nuevo
        pass

    def menu_item_open(self):
        """Abrir un Objeto.

        Realiza todas las operaciones para abrir un Objeto.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Archivo/Abrir
        pass

    def menu_item_save(self):
        """Guardar un Objeto.

        Realiza todas las operaciones para guardar un Objeto.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Archivo/Guardar
        pass

    def menu_item_cut(self):
        """Corta al portapapeles.

        Lo que hay seleccionado lo pasa al portapapeles para usarlo despúes, borrando la selección.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Editar/Cortar
        pass

    def menu_item_copy(self):
        """Copia al portapapeles.

        Lo que hay seleccionado lo pasa al portapapeles para usarlo despúes, sin borrar la selección.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Editar/Copiar
        pass

    def menu_item_paste(self):
        """Pega el portapapeles.

        Lo que hay en el portapapeles se usa para ponerlo en donde se encuentra el cursor.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Editar/Pegar
        pass

    def menu_item_show_tools_bar(self):
        """Mostrar/Ocultar barra de herramientas.

        Con esta opción podemos mostrar u ocultar la barra de herramientas.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Ver/Mostrar barra de herramientas
        pass

    def menu_item_show_status_bar(self):
        """Mostrar/Ocultar barra de estado.

        Con esta opción podemos mostrar u ocultar la barra de estado.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Ver/Mostrar barra de estado
        pass

    def menu_item_other(self):
        """Detener la aplicación.

        Es para detener la aplicación desde el menu Archivo/Salir.
        """
        # FIXME: implementar, Esto es lo que se hará al pulsar Herramientas/Utiles
        pass

    def menu_item_exit(self):
        """Detener la aplicación.

        Es para detener la aplicación desde el menu Archivo/Salir.
        """
        self.exit_application()

    def exit_application(self):
        """Detener la aplicación.

        Es para detener la aplicación.
        """
        self._window.stop()