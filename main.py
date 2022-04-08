from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 

class Increment(BoxLayout):
    pass

class Screen(App): 
    def build(self):
        return Increment()

Screen().run()
