import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


kivy.require('1.11.1')


class Container(BoxLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__()
        self.count = 0

    def opacity_btn(self):
        if self.count == 0:
            self.ids.flLayout.opacity = 1
            self.ids.boxLayIzq.opacity = 1
            self.ids.anchorLayout.opacity = 1
            self.ids.boxhorizontal.opacity = 1
            self.count = 1
        else:
            self.ids.flLayout.opacity = 0
            self.ids.boxLayIzq.opacity = 0
            self.ids.anchorLayout.opacity = 0
            self.ids.boxhorizontal.opacity = 0
            self.count = 0

class MainApp(App):
    title = 'Unidad 3'

    def build(self):
        return Container()


if __name__ == '__main__':
    app = MainApp()
    app.run()