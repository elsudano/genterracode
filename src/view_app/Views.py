#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""Diferent views of the application.

Here we can create all the views that we will need for our application.
"""

from src.view_app.View import *

class MainView(View):
    """Main View"""

    def _init_view(self):
        """Initialating the view.
        """
        self._change_size(300,170)
        self._default_config()
        # --------------------------------------------------------------------------------
        self.b_using_openai_api = ttk.Button(self._principal_frame, text="Use OpenAI API")
        self.b_using_openai_api.grid(column=0, row=0, sticky='NW')
        self.b_using_openai_api.bind("<Button>", self._controller.using_openai_api)
        self.b_two = ttk.Button(self._principal_frame, text="Button Two")
        self.b_two.grid(column=0, row=1, sticky='NW')
        self.b_two.bind("<Button>", self._controller.two)
        self.b_three = ttk.Button(self._principal_frame, text="Button Three")
        self.b_three.grid(column=0, row=2, sticky='NW')
        self.b_three.bind("<Button>", self._controller.three)

class FirstView(View):
    """First View"""

    def _init_view(self):
        """Initialating the view.
        """
        self._change_size(800,300)
        self._default_config()
        # ----------------------------------------------------------------------------------
        self.t_question = text(self._principal_frame, relief='solid')
        self.t_question.grid(column=0, row=0, columnspan=12, sticky='NESW')
        self.l_answer = ttk.Label(self._principal_frame, relief='solid', text="Request Answer")
        self.l_answer.grid(column=0, row=1, columnspan=12, sticky='NESW')
        self.b_submit = ttk.Button(self._principal_frame, text="Request Answer")
        self.b_submit.grid(column=0, row=2, sticky='NESW')
        self.b_submit.bind("<Button>", self._controller.request_answer)
        self.b_reset = ttk.Button(self._principal_frame, text="Reset Tokens")
        self.b_reset.grid(column=1, row=2, sticky='NESW')
        self.b_reset.bind("<Button>", self._controller.reset)
        self.b_help = ttk.Button(self._principal_frame, text="I need help")
        self.b_help.grid(column=2, row=2, sticky='NESW')
        self.b_help.bind("<Button>", self._controller.openai_help)

    def get_question(self):
        return self.t_question.get('1.0', constants.END)
    
    def reset_question(self):
        self.t_question.delete('1.0', constants.END)

    def set_question(self, question):
        self.t_question.delete('1.0', constants.END)
        self.t_question.insert('1.0', question)
    
    def set_answer(self, answer):
        self.l_answer.config(text=answer)

class SecondView(View):
    """View to manage other things"""

    def _init_view(self):
        """Initialating the view.

        This method is the first method that we use to put all the 
        widgets in the view and start to interact with them.
        """
        # I we want to change the size of the window
        self._change_size(500,300)
        self._default_config()
        # --------------------------------------------------------------------------------
        self.b_select_audio = ttk.Button(self._principal_frame, text="Select Audio File")
        self.b_select_audio.grid(column=4, row=0, sticky='NESW')
        self.b_select_audio.bind("<Button>", self._controller.back)
        self.cb_noise_signal = ttk.Checkbutton(self._principal_frame, text="ruido en sonido", variable=self._controller.back)
        self.cb_noise_signal.grid(column=4, row=1, sticky='NESW')
        self.e_digits = ttk.Entry(self._principal_frame)
        self.e_digits.grid(column=4, row=2, sticky='NESW')
        self.b_encode = ttk.Button(self._principal_frame, text="Encode Digits")
        self.b_encode.grid(column=4, row=3, sticky='NESW')
        self.b_encode.bind("<Button>", self._controller.back)
        self.b_decode = ttk.Button(self._principal_frame, text="Decode Tones")
        self.b_decode.grid(column=4, row=4, sticky='NESW')
        self.b_decode.bind("<Button>", self._controller.back)
        self.b_ejercicio2 = ttk.Button(self._principal_frame, text="Ejercicio 2")
        self.b_ejercicio2.grid(column=0, columnspan=4, row=0, sticky='NESW')
        self.b_ejercicio2.bind("<Button>", self._controller.back)
        # inicializamos todas las variables para los checkbuttons
        for x in range(0, 8):
            self._controller._num_signal[x] = IntVar()
        self.cb_signal1 = ttk.Checkbutton(self._principal_frame, text="1ra", variable=self._controller._num_signal[0])
        self.cb_signal1.grid(column=0, row=1, sticky='E')
        self.cb_signal2 = ttk.Checkbutton(self._principal_frame, text="2da", variable=self._controller._num_signal[1])
        self.cb_signal2.grid(column=1, row=1, sticky='E')
        self.cb_signal3 = ttk.Checkbutton(self._principal_frame, text="3ra", variable=self._controller._num_signal[2])
        self.cb_signal3.grid(column=2, row=1, sticky='E')
        self.cb_signal4 = ttk.Checkbutton(self._principal_frame, text="4ta", variable=self._controller._num_signal[3])
        self.cb_signal4.grid(column=3, row=1, sticky='E')
        self.cb_signal5 = ttk.Checkbutton(self._principal_frame, text="5ta", variable=self._controller._num_signal[4])
        self.cb_signal5.grid(column=0, row=2, sticky='E')
        self.cb_signal6 = ttk.Checkbutton(self._principal_frame, text="6ta", variable=self._controller._num_signal[5])
        self.cb_signal6.grid(column=1, row=2, sticky='E')
        self.cb_signal7 = ttk.Checkbutton(self._principal_frame, text="7ma", variable=self._controller._num_signal[6])
        self.cb_signal7.grid(column=2, row=2, sticky='E')
        self.cb_signal8 = ttk.Checkbutton(self._principal_frame, text="8va", variable=self._controller._num_signal[7])
        self.cb_signal8.grid(column=3, row=2, sticky='E')
        self.b_ejercicio3 = ttk.Button(self._principal_frame, text="Ejercicio 3")
        self.b_ejercicio3.grid(column=0, columnspan=4, row=3, sticky='NESW')
        self.b_ejercicio3.bind("<Button>", self._controller.back)

class ThirdView(View):
    """View to manage other things"""

    def _init_view(self):
        """Initialating the view.

        This method is the first method that we use to put all the 
        widgets in the view and start to interact with them.
        """
        # Modificamos el tamaño de la ventana en esta vista
        self._change_size(520,150)
        self._default_config()
        # --------------------------------------------------------------------------------
        self.b_task01 = ttk.Button(self._principal_frame, text="Ejercicio 1 Punto 1")
        self.b_task01.grid(column=0, row=0, sticky='NESW')
        self.b_task01.bind("<Button>", self._controller.back)
        self.b_task02 = ttk.Button(self._principal_frame, text="Ejercicio 1 Punto 2")
        self.b_task02.grid(column=0, row=1, sticky='NESW')
        self.b_task02.bind("<Button>", self._controller.back)
        self.b_task03 = ttk.Button(self._principal_frame, text="Ejercicio 1 Punto 3")
        self.b_task03.grid(column=0, row=2, sticky='NESW')
        self.b_task03.bind("<Button>", self._controller.back)
        self.b_task04 = ttk.Button(self._principal_frame, text="Ejercicio 1 Punto 4")
        self.b_task04.grid(column=0, row=3, sticky='NESW')
        self.b_task04.bind("<Button>", self._controller.back)
        self.b_task05 = ttk.Button(self._principal_frame, text="Ejercicio 2")
        self.b_task05.grid(column=1, row=0, sticky='NESW')
        self.b_task05.bind("<Button>", self._controller.back)
        self.b_task06 = ttk.Button(self._principal_frame, text="Ejercicio 2 Punto 1")
        self.b_task06.grid(column=1, row=1, sticky='NESW')
        self.b_task06.bind("<Button>", self._controller.back)
        self.b_task07 = ttk.Button(self._principal_frame, text="Ejercicio 2 Punto 2")
        self.b_task07.grid(column=1, row=2, sticky='NESW')
        self.b_task07.bind("<Button>", self._controller.back)
        self.b_task08 = ttk.Button(self._principal_frame, text="Ejercicio 2 Punto 3")
        self.b_task08.grid(column=1, row=3, sticky='NESW')
        self.b_task08.bind("<Button>", self._controller.back)
        self.b_task09 = ttk.Button(self._principal_frame, text="Ejercicio 3")
        self.b_task09.grid(column=2, row=0, sticky='NESW')
        self.b_task09.bind("<Button>", self._controller.back)
        self.b_task10 = ttk.Button(self._principal_frame, text="Ejercicio 3 Punto 1")
        self.b_task10.grid(column=2, row=1, sticky='NESW')
        self.b_task10.bind("<Button>", self._controller.back)
        self.b_task11 = ttk.Button(self._principal_frame, text="Ejercicio 3 Punto 2")
        self.b_task11.grid(column=2, row=2, sticky='NESW')
        self.b_task11.bind("<Button>", self._controller.back)
        self.b_task12 = ttk.Button(self._principal_frame, text="Ejercicio 4 Punto 1")
        self.b_task12.grid(column=3, row=0, sticky='NESW')
        self.b_task12.bind("<Button>", self._controller.back)
        self.b_task13 = ttk.Button(self._principal_frame, text="Ejercicio 4 Punto 2")
        self.b_task13.grid(column=3, row=1, sticky='NESW')
        self.b_task13.bind("<Button>", self._controller.back)
        self.b_task14 = ttk.Button(self._principal_frame, text="Ejercicio 4 Punto 3")
        self.b_task14.grid(column=3, row=2, sticky='NESW')
        self.b_task14.bind("<Button>", self._controller.back)
        self.b_task15 = ttk.Button(self._principal_frame, text="Ejercicio 4 Punto 4")
        self.b_task15.grid(column=3, row=3, sticky='NESW')
        self.b_task15.bind("<Button>", self._controller.back)
