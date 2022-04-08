from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 

class TasksList(BoxLayout):
    def __init__(self, tasks, **kwargs):
        super().__init__(**kwargs)
        for task in tasks:
            self.ids.box.add_widget(Task(text=task))

    def addWidget(self):
        text = self.ids.task_input.text
        self.ids.box.add_widget(Task(text = text))
        self.ids.task_input.text = ''

class Task(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label_task.text = text

class Screen(App): 
    def build(self):
        return TasksList(['Go shopping', 'Pick up the kids', 'Walk the dog', 'Study for exames', 'Read a book'])

Screen().run()
