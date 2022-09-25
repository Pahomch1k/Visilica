from ast import While
import random
from urllib import request
  
def print_word(word_to_guess, letters_used):
    global correct_letters
    for ch in word_to_guess:
        if ch in letters_used:
            print(f"{ch}", end = '')
            correct_letters += 1
        else:
            print("_", end = '')
    print()
 
URL = 'https://random-word-api.herokuapp.com/word' 
resp = request.urlopen(URL)

array_words = []

lol = 1
while lol < 10:
    data = resp.read() 
    str = data.decode("UTF-8") 
    array_words.append(str)
    lol += 1
 
word_to_guess = array_words[random.randint(0,4)] 
letters_used = ""

failed_attempts = 0
count = 6;
while failed_attempts < 6:
    letter = input("Enter your letter: ")
    letters_used += letter.lower()

    if letter.lower() in word_to_guess:
        print(f"Well done! Letter {letter.lower()} is present in this word")
    else:
        print(f"Sorry! You are wrong :(")
        failed_attempts += 1

    print(f"Осталось {count - failed_attempts} попыток") 
    print(f"Вы использовали такие буквы - {letters_used}") 

    correct_letters = 0

    print_word(word_to_guess, letters_used)

    if correct_letters == len(word_to_guess):
        print(f"Great! You won! The word is {word_to_guess}")
        break
else: 
    print("Sorry, you lost!")
    print(" $$$$$     $$$$$     ") 
    print("$         $       ") 
    print("$  $$$$   $  $$$$         ") 
    print(" $   $$$   $   $$$      ") 
    print("  $$$$$     $$$$$  ") 
