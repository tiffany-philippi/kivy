from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class Manager(ScreenManager):
    pass

class Menu(Screen):
    pass

class TasksList(Screen):
    def __init__(self, tasks=[], **kwargs):
        super().__init__(**kwargs)
        for task in tasks:
            self.ids.box.add_widget(Task(text=task))

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.back)

    def back(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.back)

    def addWidget(self):
        text = self.ids.task_input.text
        self.ids.box.add_widget(Task(text = text))
        self.ids.task_input.text = ''

class Task(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label_task.text = text

class View(App): 
    def build(self):
        return Manager()

View().run()
