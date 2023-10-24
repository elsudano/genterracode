#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Model of data.

This is the root part of our model of data, we can use this file
like a storage where we need put all our libraries.
"""
# para crear clases con padres e hijos
from abc import ABC, abstractmethod
# para la reproducción de sonidos
# from pydub import AudioSegment as mix
# from pydub.playback import play
# # para calculos matematicos
# from scipy import signal
# from scipy.io import wavfile
# # para tratamiento de imagenes
# from scipy.misc import imread, imsave, imresize, imrotate, imshow
# para valores random de las señales
import random
#
import struct
# import matplotlib
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import numpy
import openai
import os
import sys
#
class Model(ABC):
    """Model class."""

    def __init__(self):
        """Construct by default."""
        pass

    @abstractmethod
    def _init_model(self):
        pass
