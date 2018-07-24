import os
import shutdown
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.theming import ThemeManager
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivymd.toolbar import Toolbar
from navigationdrawer import NavigationDrawer
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from bmconfigparser import BMConfigParser
from kivy.properties import BooleanProperty
statusIconColor = 'red'


class NavigateApp(App, TextInput):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def build(self):
        main_widget = Builder.load_file(os.path.join(os.path.dirname(__file__), 'main.kv'))
        self.nav_drawer = Navigator()
        return main_widget

    def say_exit(self):
        print ("**************************EXITING FROM APPLICATION*****************************")
        App.get_running_app().stop()
        shutdown.doCleanShutdown()


class Navigator(NavigationDrawer):
    image_source = StringProperty('images/me.jpg')
    title = StringProperty('Navigation')


class Inbox(Screen):
    def __init__(self, **kwargs):
        super(Inbox, self).__init__(**kwargs)
        val_y = .1
        val_z = 0
        my_box1 = BoxLayout(orientation='vertical')
        for i in range(1, 5):
            my_box1.add_widget(Label(text="I am in inbox", size_hint = (.3,.1), pos_hint = {'x': val_z,'top': val_y},color = (0,0,0,1), background_color = (0,0,0,0)))
            val_y += .1
        self.add_widget(my_box1)


class Sent(Screen):
    def __init__(self, **kwargs):
        super(Sent, self).__init__(**kwargs)
        val_y = .1
        val_z = 0
        my_box1 = BoxLayout(orientation='vertical')
        for i in range(1, 5):
            my_box1.add_widget(Label(text="I am in sent", size_hint = (.3,.1), pos_hint = {'x': val_z,'top': val_y},color = (0,0,0,1), background_color = (0,0,0,0)))
            val_y += .1
        self.add_widget(my_box1)


class Trash(Screen):
    def __init__(self, **kwargs):
        super(Trash, self).__init__(**kwargs)
        val_y = .1
        val_z = 0
        my_box1 = BoxLayout(orientation='vertical')
        for i in range(1, 5):
            my_box1.add_widget(Label(text="I am in trash", size_hint = (.3,.1), pos_hint = {'x': val_z,'top': val_y},color = (0,0,0,1), background_color = (0,0,0,0)))
            val_y += .1
        self.add_widget(my_box1)


class Dialog(Screen):
    pass


class Test(Screen):
    pass


class Create(Screen, Widget):

    def __init__(self, *args, **kwargs):
        super(Create, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.init_ui, 0)

    def init_ui(self, dt=0):
        # self.ids['recipent'].bind(text=self.on_text)
        pass

    def showmeaddresses(self):
        return BMConfigParser().addresses()

    def send(self):
        pass


class NewIdentity(Screen):
    is_active = BooleanProperty(False)

if __name__ == '__main__':
    NavigateApp().run()