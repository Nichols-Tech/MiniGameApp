from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
import random


class ColorGame(App):
    COLORS = [
        ('Red', '#FF0000'),
        ('Orange', '#FFA500'),
        ('Yellow', '#FFFF00'),
        ('Green', '#00FF00'),
        ('Blue', '#0000FF'),
        ('Purple', '#800080')
    ]

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.score = 0

        self.color_label = Button(text="", font_size=30)
        layout.add_widget(self.color_label)

        self.point_label = Button(text="Score: 0", font_size=20)
        layout.add_widget(self.point_label)

        color_buttons_layout = BoxLayout()

        self.color_buttons = []
        for color_name, color_code in self.COLORS:
            button = Button(background_color=get_color_from_hex(color_code), on_release=self.check_color)
            color_buttons_layout.add_widget(button)
            self.color_buttons.append(button)

        layout.add_widget(color_buttons_layout)

        self.generate_random_color()

        return layout

    def generate_random_color(self):
        color_name, color_code = random.choice(self.COLORS)
        self.color_label.text = color_name
        self.color_label.background_color = get_color_from_hex(color_code)

    def check_color(self, button):
        selected_color = None
        for color_name, color_code in self.COLORS:
            if button.background_color == get_color_from_hex(color_code):
                selected_color = color_name
                break

        if selected_color == self.color_label.text:
            self.score += 1
        else:
            self.score -= 1

        self.point_label.text = "Score: " + str(self.score)
        self.generate_random_color()


if __name__ == "__main__":
    ColorGame().run()





