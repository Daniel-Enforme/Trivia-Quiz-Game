# game/quiz.py


import sys
import os
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))

from data.questions import questions  # Import the question pool
from questions import questions


def get_questions(category, num_questions=30):
    # Fetch the questions for a specific category
    category_questions = questions.get(category, [])
    random.shuffle(category_questions)  # Shuffle the questions to randomize the order
    return category_questions[:num_questions]  # Return the first 'num_questions'

def start_quiz():
    print("Welcome to the Trivia Quiz Game!")
    
    while True:
        print("\nChoose a category:")
        print("1. Programmers")
        print("2. Computer Science")
        print("3. General Knowledge")
        print("4. Technology")

        category_choice = input("Enter the category number: ")

        if category_choice == "1":
            category = "Programmers"
        elif category_choice == "2":
            category = "Computer Science"
        elif category_choice == "3":
            category = "General Knowledge"
        elif category_choice == "4":
            category = "Technology"
        else:
            print("Invalid choice, please select again.")
            continue

        questions_list = get_questions(category)

        score = 0
        for i, question in enumerate(questions_list, 1):
            print(f"\nQ{i}: {question['question']}")
            for idx, option in enumerate(question['options'], 1):
                print(f"{idx}. {option}")
            
            answer = input("Your answer: ").strip().lower()
            
            # Check if the answer is correct
            correct_answer = question['answer'].lower()
            if answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {correct_answer.capitalize()}.")

        print(f"\nYour final score is {score}/{len(questions_list)}.")

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    start_quiz()
