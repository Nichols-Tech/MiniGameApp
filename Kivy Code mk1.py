from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import random


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        label = Label(text="Welcome to Myra's app!")
        layout.add_widget(label)

        questions = [
            ("What color is the sun?", "yellow"),
            ("How many legs does a cat have?", "four"),
            ("What animal says 'meow'?", "cat"),
            ("How many fingers do you have on one hand?", "five"),
            ("What shape is a circle?", "round"),
            ("What is the color of an orange?", "orange"),
            ("What do you call a baby cat?", "kitten"),
            ("How many wheels does a bicycle have?", "two"),
            ("What is the opposite of cold?", "hot"),
            ("How many sides does a triangle have?", "three"),
            ("What do cows drink?", "water"),
            ("What is the color of grass?", "green"),
            ("How many days are there in a week?", "seven"),
            ("What sound does a dog make?", "bark"),
            ("What is the name of the tallest animal in the world?", "giraffe"),
            ("What is the color of a banana?", "yellow"),
            ("How many eyes do you have?", "two"),
            ("What do birds use to fly?", "wings"),
            ("What is the color of the sky on a sunny day?", "blue"),
            ("What do you call the season after summer?", "autumn")
        ]

        random.shuffle(questions)

        question_label = Label(text=questions[0][0])
        layout.add_widget(question_label)

        answer_input = TextInput(multiline=False)
        layout.add_widget(answer_input)

        result_label = Label(text="")
        layout.add_widget(result_label)

        def check_answer(instance):
            user_answer = answer_input.text
            if user_answer.lower() == questions[0][1]:
                result_label.text = "Good job!"
            else:
                result_label.text = "Incorrect. Please try again."

        answer_button = Button(text="Submit Answer")
        answer_button.bind(on_release=check_answer)
        layout.add_widget(answer_button)

        def next_question(instance):
            questions.pop(0)
            answer_input.text = ""
            result_label.text = ""
            if len(questions) > 0:
                question_label.text = questions[0][0]
            else:
                layout.clear_widgets()
                layout.add_widget(Label(text="Quiz completed. Well done Myra!"))

        next_button = Button(text="Next Question")
        next_button.bind(on_release=next_question)
        layout.add_widget(next_button)

        return layout


if __name__ == "__main__":
    MyApp().run()



