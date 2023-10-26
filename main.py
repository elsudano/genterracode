#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""Main file of the application.

We have to start here to load all the objects that we have in the application.
"""

import src.view_app.Window as w
from src.controller.Controllers import MainController
from src.model.Models import MainModel
from src.view_app.Views import MainView

if __name__ == '__main__':
    # Creating the main window.
    myWindow = w("My first Application of AI", 300, 170)
    # Creating the empty model.
    myModel = MainModel()
    # Creating the main controler and adding the model in the window.
    myController = MainController(myWindow, myModel)
    # Creating the main view and adding the controller in the main window.
    myView = MainView(myWindow, myController)
    # Adding the main view in the main controller.
    myController.set_view(myView)
    # Now we can initialize the view.
    myView.init_view()
    # And finally we can show the window.
    myWindow.start()

