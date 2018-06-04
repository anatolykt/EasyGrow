import os

try:
    from kivy.lang import Builder
    from kivy.uix.floatlayout import FloatLayout
    from kivy.properties import ObjectProperty, StringProperty
except Exception as exc:
    raise exc


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    Builder.load_file(base_dir + "/kv/bugreporter.kv")
else:
    Builder.load_file("Libs/uix/kv/bugreporter.kv")


class BugReporter(FloatLayout):
    title = StringProperty("Bug reporter")

    heading = StringProperty("Sorry, error occurred")
    subheading = StringProperty("To fix it shortly, please report this bug")
    error_traceback = StringProperty("")

    exit_button_text = StringProperty("Exit")
    exit_callback = ObjectProperty(None)

    report_button_text = StringProperty("Report")
    report_callback = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(BugReporter, self).__init__(**kwargs)
        self.exit_callback = self.exit

    def exit(self, *args):
        from kivy.app import App
        App.get_running_app().stop()


if __name__ == "__main__":
    from kivy.app import App
    from kivy.core.window import Window
    from kivymd.theming import ThemeManager

    Window.size = (375, 667)

    class Debug(App):
        title = "Bug reporter"
        theme_cls = ThemeManager()
        def build(self):
            return BugReporter(report_callback=activity)

    Debug().run()