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
from kivy.uix.image import Image, AsyncImage
from kivy.uix.screenmanager import ScreenManager, Screen


class VideoGrid(GridLayout):
    pass
    def __init__(self, **kwargs):
        super(VideoGrid, self).__init__(**kwargs)
        self.cols = 4
        self.farva = AsyncImage(source='http://download.gamezone.com/uploads/image/data/1115062/super_trooper_car_ramrod.jpg',  color=[1,0,0,1], size_hint=(0.4,0.4), pos_hint={'x':0.3, 'y':0.3})
        self.add_widget(self.farva)


class SettingsGrid(GridLayout):
    pass
    # def __init__(self, **kwargs):
    #     super(SettingsGrid, self).__init__(**kwargs)
    #     self.cols = 2
    #
    #     self.add_widget(Label(text='Evergreen URL:'))
    #
    #     self.url = TextInput(multiline=False)
    #     self.add_widget(self.url)


class Float(FloatLayout):
    pass


class SettingsScreen(Screen):
    pass


class VideoScreen(Screen):
    pass


class EvergreenNewReleases(App):
    def open_settings(self, *args):
        self.sm.current = 'settings_screen'

    def build(self):
        # floater = Float()
        self.sm = ScreenManager()
        video_screen = VideoScreen(name='video_screen')
        settings_screen = SettingsScreen(name='settings_screen')

        # self.pole_cats = Image(source='img/pole_cats.jpg', color=[1,0,0,1], size_hint=(0.5,0.5), pos_hint={'x':0, 'y':0})
        # # floater.add_widget(self.pole_cats)
        #
        # self.farva = AsyncImage(source='http://download.gamezone.com/uploads/image/data/1115062/super_trooper_car_ramrod.jpg',  color=[1,0,0,1], size_hint=(0.4,0.4), pos_hint={'x':0.3, 'y':0.3})
        # floater.add_widget(self.farva)

        # floater.add_widget(SettingsGrid())
        # floater.add_widget(VideoGrid())

        self.sm.add_widget(video_screen)
        self.sm.add_widget(settings_screen)
        video_screen.add_widget(Button(text='Settings', on_press=self.open_settings))

        # settings_screen.add_widget(Button(text='Back', on_press=self.open_settings, ))

        return self.sm


if __name__ == '__main__':
    EvergreenNewReleases().run()
