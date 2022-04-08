from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout 

class Screen(App): 
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text="How many times did I click?", font_size=30, on_release=self.increment)
        self.label = Label(text="0", font_size=21)
        box.add_widget(button)
        box.add_widget(self.label)
        
        return box

    def increment(self, button):
        self.label.text = str(int(self.label.text)+1)

Screen().run()
