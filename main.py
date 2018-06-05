import os
import sys
import traceback


ERROR_LOG = os.getenv("ERROR_LOG") or (len(sys.argv) > 1 and sys.argv[1]) or "./error.log"
PROJ_REPO = os.getenv("PROJ_REPO") or (len(sys.argv) > 2 and sys.argv[2])

try:
	import kivy
	kivy.require("1.10.0")

	import kivymd
	from kivy.app import App
	from kivy.config import Config
	from kivy.core.window import Window

	Window.size = (375, 667)
	Config.set("kivy", "keyboard_mode", "system")
	from Libs.uix.bugreporter import BugReporter

except Exception:
	traceback.print_exc(file=open(ERROR_LOG, "w"))
	sys.exit(1)


__version__ = "0.0.1"

def main():
	app = None

	try:
		from program import Program

		app = Program()
		app.run()

	except Exception as exc:
		traceback.print_exc(file=open(ERROR_LOG, "w"))

		class Error(App):
			theme_cls = kivymd.theming.ThemeManager()

			def report_callback(self, *args):
				try:
					import webbrowser
					webbrowser.open(
						PROJ_REPO + "/issues/new?body=" + str(exc))
				except Exception:
					traceback.print_exc(file=open(ERROR_LOG, "w"))
					sys.exit(1)

			def build(self):
				return BugReporter(
					report_callback=self.report_callback)

		Error().run()


if __name__ == "__main__":
	main()