############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.
from art import logo
import random
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##Ask for input
answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if answer == 'y':
  print(logo)

  playercards = []
  playercards = playercards + [random.choice(cards)]
  playercards = playercards + [random.choice(cards)]
  
  current_score = sum(playercards)
  
  computercards = []
  computercards = computercards + [random.choice(cards)]
  computercards = computercards + [random.choice(cards)]

  current_comp_score = sum(computercards)

  player_blackjack = False
  if current_score == 21:
    player_blackjack = True

  computer_blackjack = False
  if current_comp_score == 21:
    computer_blackjack = True

  if player_blackjack == True:
    if computer_blackjack == False:
      print(f"  Your cards: [{playercards[0]}, {playercards[1]}], current score: {current_score}")
      print(f"  Computer's first card: {computercards[0]}")
      print(f"  Your final hand: {playercards}, final score: {current_score}")
      print(f"  Computer's final hand: {computercards}, final score: {current_comp_score}")
      print("Win with a Blackjack 😎")
    elif computer_blackjack == True:
      print(f"  Your cards: [{playercards[0]}, {playercards[1]}], current score: {current_score}")
      print(f"  Computer's first card: {computercards[0]}")
      print(f"  Your final hand: {playercards}, final score: {current_score}")
      print(f"  Computer's final hand: {computercards}, final score: {current_comp_score}")
      print("Lose, opponent has Blackjack 😱")
  
  print(f"  Your cards: [{playercards[0]}, {playercards[1]}], current score: {current_score}")
  print(f"  Computer's first card: {computercards[0]}")

  should_end = False
  
  while should_end == False:
    continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
    if continue_game == 'y':
      next_card = random.choice(cards)
      playercards = playercards + [next_card]
      if next_card == 11 and sum(playercards) > 21:
          next_card == 1
      current_score = sum(playercards)
      if current_score > 21:
        should_end = True
        computercards = computercards + [random.choice(cards)]
        current_comp_score = sum(computercards)
        print(f"  Your cards: {playercards}, current score: {current_score}")
        print(f"  Computer's first card: {computercards[0]}")
        print(f"  Your final hand: {playercards}, final score: {current_score}")
        print(f"  Computer's final hand: {computercards}, final score: {current_comp_score}")
        print("You went over. You lose 😭")

      else:
        print(f"  Your cards: {playercards}, current score: {current_score}")
        print(f"  Computer's first card: {computercards[0]}")

    else:
      while current_comp_score < 17:
        computercards = computercards + [random.choice(cards)]
        current_comp_score = sum(computercards)  
        print(f"  Your final hand: {playercards}, final score: {current_score}")
        print(f"  Computer's final hand: {computercards}, final score: {current_comp_score}")
      should_end = True

    if current_score > current_comp_score:
      print("You win 😃")
    elif current_score == current_comp_score:
      print("Draw 🙃")
    else:
      print("You lose 😤")
    
else: 
  print("")

        
  
