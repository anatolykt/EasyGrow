from kivy.app import App
from kivymd.theming import ThemeManager

from Libs.uix.home import HomeScreen
from Libs.uix.initial import InitialScreen


class Program(App):
	theme_cls = ThemeManager()

	def build(self):
		return HomeScreen()