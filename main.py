import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class Calculator(Widget):
    def add(self, num):
        if not self.screen.text and num in ["+", "-", "*", "/"]:
            self.screen.text += self.result.text + num
            return
        self.screen.text += num
    def calculate(self):
        if len(self.screen.text) > 0:
            self.result.text = str(eval(self.screen.text))
            self.screen.text = ""

class Calc(App):
    def build(self):
        return Calculator()


if __name__ == '__main__':
    Calc().run()