"""
blackjack.py (12 points)
=====

Complete the program below to simulate a single hand of blackjack. The code for
creating a deck of cards and dealing cards is written for you. You can see the
slides discussing the code here:

http://foureyes.github.io/csci-ua.0002-spring2015-007/classes/20/lists_strings_random.html#5.0

Of course, the obligatory wikipedia article:

http://en.wikipedia.org/wiki/Blackjack

Add the following features to the program:

* continually ask the player whether they want to draw another card (hit) or
  stop drawing cards (stand)
* after either hitting or standing, calculate the total and display the
  player's last action, their hand and their hand's total (use the function
  written underneath the comments to run this calculation):

  (Player draws another card)
  Player Hand: ['2', 'J']
  Player Total: 12
  
* if the total of the player's cards are over 21, or if the player's says
  stand, stop asking the player whether they want to hit or stand
* if the player's cards are over 21, print out "BUST!"
* once the player is done drawing (or if they go over 21), populate the
  computer's hand by automatically removing cards from the deck and adding them to the computer's
  to the computer's hand until the total for the computer's hand is > 17
* determine who won:
  * the player who is the closest to 21 without going over wins
  * a ties is possible

Here's an example of run of the program:
=====

Player Hand: ['2', 'J']
Player Total: 12

(h)it or (s)tand?
> h

(Player draws another card)
Player Hand: ['2', 'J', '7']
Player Total: 19

(h)it or (s)tand?
> s

(Player stands)
Player Hand: ['2', 'J', '7']
Player Total: 19

Computer Hand: ['K', '6', '8']
Computer Total: 24

Player won!
=====

Another example with the player going over 21:
=====
Player Hand: ['J', '7']
Player Total: 17

(h)it or (s)tand?
> h

(Player draws another card)
Player Hand: ['J', '7', 'Q']
Player Total: 27
BUST

Computer Hand: ['Q', 'A']
Computer Total: 21

Computer won!
"""

import random

def current_total(hand):
    """ Sums the cards in hand.  Aces count as 1 or 11.  Will optimize for 
    highest total without going over 21.
    """
    total, aces = 0, 0
    for card in hand:
        if card.isdigit():
            total += int(card)
        elif card in 'JQK':
            total += 10
        elif card == 'A':
            aces += 1
            total += 11
    for i in range(aces):
        if total > 21:
            total -= 10
    return total


    
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)
player_hand = []
computer_hand = []
for i in range(2):
    player_hand.append(deck.pop())
    computer_hand.append(deck.pop())


# Use the function, current_total, and the variables defined above to
# finish this implementation of one "hand" of blackjack

# 1. continually ask whether or not the player wants to it or stand
# 2. once the player is done drawing cards (or if they go over 21)...
#    continually remove cards from the deck and add them to the computer's
#    hand until the computer's hand total is over 17
# 3. the player that's closest to 21 without going over wins

print("player hand: %s" % player_hand)
print("player total: %s \n" % current_total(player_hand))

while True:
    keep_going = input("(h)it or (s)tand?\n>")
    if keep_going == "h":
        player_hand.append(deck.pop())
        print("\n(Player draws another hand)")
        print("player hand: %s" % player_hand)
        print("player total: %s" % current_total(player_hand))
        if current_total(player_hand) > 21:
            print("BUST")
            break
    elif keep_going == "s":
        print("\n(Player stands)")
        print("player hand: %s" % player_hand)
        print("player total: %s" % current_total(player_hand))
        break

while current_total(computer_hand) < 18:
    computer_hand.append(deck.pop())

print("\ncomputer hand: %s" % computer_hand)
print("computer total: %s" % current_total(computer_hand))

if current_total(computer_hand) > 21 and current_total(player_hand) > 21:
    print("\nNobody wins!")
elif 21 - current_total(computer_hand) > 21 - current_total(player_hand):
    print("\nComputer wins!")
elif 21 - current_total(player_hand) > 21 - current_total(computer_hand):
    print("\nPlayer wins!")
elif current_total(player_hand) == current_total(computer_hand):
    print("\nTie!")




       

