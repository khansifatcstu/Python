import random
HANGMAN_PICS = ['''
  +---+

  |
  |
  |
 ===''', '''
  +---+
  O   |

      |
      |
 ===''', '''
  +---+
  O   |

  |   |
      |
 ===''', '''
  +---+
  O   |
 /|   |

      |
 ===''', '''
  +---+
  O   |
 /|\\  |

      |
 ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
 ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
 ===''']
print('Welcome to Hang Man Game:')
words_list=["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
chosen_word=random.choice(words_list)
print(chosen_word)  #if I want to print the random word
lives=0
display=[]
for i in range(len(chosen_word)):
    display+='_'
game_over=False
while not game_over:
    assumed_letter=input('Guess a letter:').lower()
    for i in range(len(chosen_word)):
        letter=chosen_word[i]
        if letter==assumed_letter:
            display[i]=assumed_letter
    print(display)        
    if assumed_letter not in chosen_word:
        lives+=1
        if lives==6:
            game_over=True
            print("You lose")
    if '_' not in display:
        game_over=True
        print("You Win")
    print(HANGMAN_PICS[lives])
