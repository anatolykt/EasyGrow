import os
import sys
import traceback

sys.dont_write_byte_code = True

try:
	import kivy
	kivy.requre("1.10.0")

	from kivy.app import App
	from kivy.config import Config

	# Устанавливаю системную клавиатуру
	# устройства для ввода информации.
	Config.set("kivy", "keyboard_mode", "system")
except Exception:
	print("{}".format(traceback.format_exc()))
	sys.exit(1)


__version__ = "0.0.1"


def main():
	""" Точка входа в приложение """
	app = None

	try:
		from program import Program
		app = Program()
		app.run()
	except Exception as exc:
		print(traceback.format_exc())
		traceback.print_exc(file=open("{}/error.log".format(
			os.path.split(os.path.abspath(sys.argv[0]))[0]), "w"))

		if app:
			app.stop()

		class Error(App):
			def callback_report(self, *args):
				import webbrowser
				import six.moves.urllib
				pass