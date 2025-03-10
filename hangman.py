import random

four_letter_word_bank = ['code', 'pool', 'toad', 'road', 'fool']
five_letter_word_bank = ['table', 'smart', 'fight', 'party', 'study']

print('Welcome to Hangman!')
print('Enter 4 for a four letter word.')
print('Enter 5 for a five letter word.')
choice = int(input('Your choice: '))

if choice == 4:
  word = random.choice(four_letter_word_bank)
elif choice == 5:
  word = random.choice(five_letter_word_bank)
else:
  print('Invalid input.')
  exit()

guessedWord = ['_'] * len(word)
attempts = 5

while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedWord))

  guess = input('Guess a letter: ').lower()
   
  if guess in word:
    for i in range(len(word)):
     if word[i] == guess:
      guessedWord[i] = guess
    print('Correct!')
  else:
    attempts -= 1
    print('Wrong guess! Attempts left: ' + str(attempts))
    
  if '_' not in guessedWord:
    print('\nCongratulations! You guessed the word: ' + word)
    break
  if attempts == 0:
    print('\nYou\'ve run out of attempts! The word was: ' + word)