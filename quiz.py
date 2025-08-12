#Python script for an irish language flashcard quiz

#importing libraries
import csv
import os
import random
import difflib
import sys


DATA_DIR = "data"

def list_categories():
    files  = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
    categories = [os.path.splitext(f)[0] for f in files]
    return categories

def choose_category():
    categories = list_categories()
    print("Choose a category: ")
    for i, cat in enumerate(categories, 1 ):
        print(f"{i}. {cat}")
    while True:
        choice = input("Enter number: ").strip()
        if not choice.isdigit():
            print("Please enter a number.")
            continue
        choice_num = int(choice)
        if 1 <= choice_num <= len(categories):
            return os.path.join(DATA_DIR, categories[choice_num - 1] + ".csv")
        else:
            print(f"Please enter a number between 1 and {len(categories)}.")

def load_flashcards(filename):
    flashcards = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # normalize keys (make sure CSV headers match these)
            flashcards.append({"Irish": row['Irish'], "English": row['English']})
    return flashcards


#quit option
def quiz_user(flashcards):
    score = 0
    answered = 0

    for card in flashcards:
        answer = input(f"What is the English for '{card['Irish']}'? ")

        cleaned = answer.strip().lower()

        if cleaned in ("quit", "q"):
            print("\nQuiz ended early.")
            print(f"Your score: {score}/{answered}")
            sys.exit()  # <-- This ends the whole program immediately


        answered += 1

        if cleaned == english.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was '{english.strip()}'.")

    print(f"\nYour score: {score}/{answered}")


def run_flashcards(flashcards):
    score = 0
    answered = 0
    random.shuffle(flashcards)
    for card in flashcards:
        answer = input(f"What is '{card['Irish']}' in English? ").strip().lower()
        if answer in ("quit", "q"):
            print("\nQuiz ended early.")
            print(f"Your score: {score}/{answered}")
            return
        answered += 1
        if answer == card['English'].lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer was: {card['English']}")
    print(f"\nFinal Score: {score}/{len(flashcards)}")



def main():
    category_file = choose_category()
    flashcards = load_flashcards(category_file)
    run_flashcards(flashcards)

if __name__ == "__main__":
    main()
