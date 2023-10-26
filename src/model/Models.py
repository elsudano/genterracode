#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""List of the models.

We have all the models that we will need in our application.
"""
from src.Constants import DEBUG
from src.model.Model import *

class MainModel(Model):
    """The main model of the application.

    With this model we can manage the behavior of our main view.
    """

    def _init_model(self):
        pass

class FirstModel(Model):
    """The main model of the application.

    With this model we can manage the behavior of our main view.
    """
    def _init_model(self):
        openai.organization = os.getenv('OPENAI_ORGANIZATION')
        openai.api_key = os.getenv('OPENAI_API_KEY')
        if DEBUG:
            print('ORG:{}, API:{}'.format(openai.organization, openai.api_key))

    def get_completion(self, prompt, model="gpt-3.5-turbo", temperature=0): 
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=100,
        )
        return response.choices[0].message['content']
    
    def openai_help(self):
        return openai.Model.list()