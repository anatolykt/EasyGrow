from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout


Builder.load_file("Libs/uix/kv/bugreporter.kv")


class BugReporter(FloatLayout):
    title = StringProperty("Bug reporter")

    heading = StringProperty("Sorry, error occurred")
    subheading = StringProperty("To fix it shortly, please report this bug")

    exit_button_text = StringProperty("Exit")
    exit_callback = ObjectProperty(None)

    report_button_text = StringProperty("Report")
    report_callback = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(BugReporter, self).__init__(**kwargs)
        self.exit_callback = self.exit

    def exit(self, *args):
        App.get_running_app().stop()