# This is the intro to Myra's app

print("Welcome to Myra's app!")

playing = input('Ready to play Myra? ')

if playing.lower() != "yes":
    quit()

import random

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

for question, answer in questions:
    # Present each question to the player
    user_answer = input(question + " ")
    # Check if the answer is correct
    if user_answer.lower() != answer:
        print("Incorrect. Please try again.")
        # Repeat the question until the correct answer is provided
        while user_answer.lower() != answer:
            user_answer = input(question + " ")
    else:
        print("Good job!")
    # Continue with the next question

print("Quiz completed. Well done Myra!")
