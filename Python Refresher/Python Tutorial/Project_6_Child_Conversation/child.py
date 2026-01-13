from random import choice

questions = ["What is your favourite colour?: ", "Why is the sky blue?: ",
             "What is your favourite food?: ", "What is your favourite sport?: ", "Why does fire hurt?: "]
question = choice(questions)

answer = input(question).strip().lower()
frustrate_answer = "just because"

while answer != frustrate_answer:
    answer = input('Why?: ').strip().lower()

print('Oh, okay...')
