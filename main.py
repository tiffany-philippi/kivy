from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout 

class Screen(App): 
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text="Hello world", font_size=30, on_release=self.increment)
        label = Label(text="This is a label", font_size=21)
        box.add_widget(button)
        box.add_widget(label)
        
        return box

    def increment(self, button):
        button.text = 'You\'re welcome'

Screen().run()
