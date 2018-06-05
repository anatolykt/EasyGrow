from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout


Builder.load_file("Libs/uix/kv/initial.kv")


class InitialScreen(FloatLayout):
	title = StringProperty("EasyGrow intialization..")
	heading = StringProperty("Автоматическая система управления \n поливом")
	
	next_page = StringProperty("")
	preload = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(InitialScreen, self).__init__(**kwargs)
		self.initialization()

	def initialization(self):
		if callable(self.preload) and self.next_page:
			loading = self.ids.loading
			loading.active = True
			loading.opacity = 1

			result = self.preload()
			self.ids.preload = result

			loading.active = False
			loading.opacity = 0

			screen_manager = self.ids.screen_manager
			screen_manager.current = next_page