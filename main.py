#Step 5

import random
from hangman_words import word_list

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guessed_letter = []
from hangman_art import logo
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess == display:
      print(guess +"You already guessed this letter")
    for guess in guessed_letter:
      if guess == guessed_letter:
        guessed_letter.append(guess)
      print(guess + "has been guessed before.")
       
    

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
      if letter not in guess:
        print(guess + " is not correct. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages
    print(stages[lives])
  
  #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    
  
