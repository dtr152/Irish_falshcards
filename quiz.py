#Python script for an irish language flashcard quiz

#importing libraries
import csv
import random
import difflib #for fuzzy matching

#load the words from csv file
with open('words.csv', newline='', encoding= 'utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    words = list(reader)

score = 0
total_questions = 10 # changeable
weak_words= [] #store question you got wrong

def ask_question(word, question_lang, answer_lang):
    """Ask a question and return True if correct, False if wrong."""
    answer = input(f"What is the {answer_lang} for '{word[question_lang]}'? ")

    similarity = difflib.SequenceMatcher(None, answer.strip().lower(), word[answer_lang].lower()).ratio()

    if similarity > 0.8:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong. The correct answer is ' {word[answer_lang]}'.")
        return False
    

#quiz loop
for i in range(total_questions): #Ask total no of questions for now
    word = random.choice(words)
    
    #randomly choose quiz direction

    if random.choice([True, False]):
       q_lang, a_lang = 'Irish', 'English'
    else:
        q_lang, a_lang = 'English', 'Irish'
    
    if ask_question(word, q_lang, a_lang):
        score += 1
    else:
        weak_words.append((word, q_lang, a_lang))

#revision of weak words
if weak_words:
    print(f"\n📚 Let's review the ones you missed:\n")
    for word, q_lang, a_lang in weak_words:
        if ask_question(word, q_lang, a_lang):
            score += 1
    

    
print(f"\nFinal score: {score} out of {total_questions + len(weak_words)}.")