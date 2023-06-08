from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window


class MyApp(App):
    def build(self):
        # Create a root widget
        root = BoxLayout(orientation='vertical')

        # Set the background image
        root.background = 'PandaBG.jpg'

        # Add other widgets to the root
        label = Label(text='Little Pandas')
        root.add_widget(label)

        return root


if __name__ == '__main__':
    MyApp().run()
