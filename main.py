from kivy.app import App
from kivy.uix.scrollview import ScrollView 
from kivy.uix.label import Label

class TasksList(ScrollView):
    def __init__(self, tasks, **kwargs):
        super().__init__(**kwargs)
        for task in tasks:
            self.ids.box.add_widget(Label(text=task, font_size = 21, size_hint_y = None, height = 200))

class Screen(App): 
    def build(self):
        return TasksList(['Go shopping', 'Pick up the kids', 'Walk the dog', 'Study for exames', 'Read a book'])

Screen().run()
