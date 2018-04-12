import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class Grid(GridLayout):
    def press_beans(self, *args):
        print('self.ids:', self.ids)


class Settings(GridLayout):
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Evergreen URL:'))

        self.url = TextInput(multiline=False)
        self.add_widget(self.url)


class Anchor(AnchorLayout):
    pass

class Float(FloatLayout):
    pass


class EvergreenNewReleases(App):
    def build(self):
        # Builder.load_file('./app.kv')
        # return Label()
        # return Settings()

        # grid = Grid(cols=3, padding=14, spacing=14)
        # grid.row_default_height = 100
        # grid.col_default_width = 75
        # grid.col_force_default = True
        # grid.row_force_default = True
        #
        # beans_button = Button(
        #     text='Beans button...',
        #     size_hint=(0.2, 0.2),
        #     on_press=grid.press_beans,
        #     pos_hint={'x': 0, 'y': 0}
        # )
        # grid.add_widget( beans_button)

        # anchor = Anchor(anchor_x='center', anchor_y='top')
        # anchor.add_widget( Button(text='center top', background_color=(1,0,0,1), size_hint=(None, None), size=(50,50) ))
        floater = Float()
        floater.add_widget(anchor)
        return floater


if __name__ == '__main__':
    EvergreenNewReleases().run()
