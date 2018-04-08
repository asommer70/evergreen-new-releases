import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class Layout(FloatLayout):
    def press_beans(self, *args):
        print('self.ids:', self.ids)


class Settings(GridLayout):
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Evergreen URL:'))

        self.url = TextInput(multiline=False)
        self.add_widget(self.url)


class EvergreenNewReleases(App):
    def build(self):
        # Builder.load_file('./app.kv')
        # return Label()
        # return Settings()
        layout = Layout()

        beans_button = Button(
            text='Beans button...',
            size_hint=(0.2, 0.2),
            on_press=layout.press_beans,
            pos_hint={'x': 0, 'y': 0}
        )
        layout.add_widget( beans_button)
        return layout


if __name__ == '__main__':
    EvergreenNewReleases().run()
