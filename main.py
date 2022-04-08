from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout 

class Screen(App): 
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text="Hello world")
        label = Label(text="This is a label")
        box.add_widget(button)
        box.add_widget(label)
        return box

Screen().run()