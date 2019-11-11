# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 02:00:36 2019

@author: Mayank Aggarwal
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_string('''
<SimpleLabel>:
    text: 'Hello Doctor'
''')


class SimpleLabel(Label):
    pass


class SampleApp(App):
    def build(self):
        return SimpleLabel()

if __name__ == "__main__":
    SampleApp().run()