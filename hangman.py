import random
from hangman_words import word_list
from hangman_art import stages
import hangman_art
print (f"{hangman_art.logo}")





for i in word_list:
    chosen_word = random.choice(word_list)
print (f"{chosen_word}")
print (f"{stages[-1]}")
display = []
for i in chosen_word:
    display += "_"
print (display)
lives = 6
while ("_" in display):
    guess = input("\nEnter any letter:").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        
        if letter == guess:
            display[i]=guess
    if guess not in chosen_word:
        lives = lives-1
        print (f"{stages[lives]}")
        print (f"Lives left:{lives}")
    print (f"{display}")
    if lives == 0:
        print ("You Lost!")
        break
else:
    print ("You won!")

