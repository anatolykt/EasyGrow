from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

from kivymd.list import IRightBody


Builder.load_file("Libs/uix/kv/home.kv")


class Toolbar(FloatLayout):
	title = StringProperty("Smart Lamp")
	title_color = ListProperty([.19607843137254904, 
		.5058823529411764, .45098039215686275, 1])

	background = ListProperty([255, 255, 255, 1])

	button_icon = StringProperty("settings")
	button_color = ListProperty([.5490196078431372, 
		.6274509803921569, .7019607843137255, 1])
	button_callback = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(Toolbar, self).__init__(**kwargs)


class HomeScreen(FloatLayout):
	pass