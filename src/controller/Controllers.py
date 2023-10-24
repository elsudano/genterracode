#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Lista de controladores del programa.

En este fichero podemos encontrarnos todos los controladores,
de todas las vistas de nuestro programa.
"""

from src.controller.Controller import Controller
from src.model.Models import *
from src.controller.Controllers import *
from src.view_app.Views import *

class MainController(Controller):

    def back(self, event):
        # in the main view, we haven't the back button
        pass

    def exit(self, event):
        self.exit_application()

    def using_openai_api(self, event):
        """Change the view.
        """
        model = FirstModel()
        controller = FirstController(self._window, model)
        view = FirstView(self._window, controller)
        controller.set_view(view)
        view.init_view()

    def two(self, event):
        """Change the view.
        """
        model = MainModel()
        controller = SecondController(self._window, model)
        view = SecondView(self._window, controller)
        controller.set_view(view)
        view.init_view()

    def three(self, event):
        """Change the view.
        """
        model = MainModel()
        controller = ThirdController(self._window, model)
        view = ThirdView(self._window, controller)
        controller.set_view(view)
        view.init_view()

class FirstController(Controller):

    def back(self, event):
        """Change the view to the main one.
        """
        model = MainModel()
        controller = MainController(self._window, model)
        view = MainView(self._window, controller)
        controller.set_view(view)
        view.init_view()

    def request_answer(self, event):
        """Thi action request a answer at OpenAI.
        
        The idea is use the LLM with OpenAI to obtain the answer a different questions
        that we want to request at ChatGPT.
        """
        tokens = self._view.get_question()
        self._model._init_model()
        answer = self._model.get_completion(prompt=tokens)
        self._view.set_answer(answer=answer)

    def reset(self, event):
        """We can clean all the data on the form.
        
        We can reset all the values in the UI in order to request the next question.
        """
        self._view.reset_question()
        self._view.set_answer(answer='')

    def openai_help(self, event):
        self._view.set_question(self._model.openai_help())

class SecondController(Controller):
    
    _num_signal = [0, 0, 0, 0, 0, 0, 0, 0]

    def back(self, event):
        """Change the view to the main one.
        """
        model = MainModel()
        controller = MainController(self._window, model)
        view = MainView(self._window, controller)
        controller.set_view(view)
        view.init_view()

class ThirdController(Controller):

    def back(self, event):
        """Change the view to the main one.
        """
        model = MainModel()
        controller = MainController(self._window, model)
        view = MainView(self._window, controller)
        controller.set_view(view)
        view.init_view()