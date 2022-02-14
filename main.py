import csv
import random 
from datetime import datetime
from helper import findScore, betterHand

#Each card is represented by a tuple {card, suit}
#((1-12), (1-4))

#Make 52 card deck
def makeDeck():
    deck = []
    for suit in range(1, 5):
        for rank in range(1, 14):
            deck.append((rank, suit))
    deck.sort()
    return deck

# Deal shuffled deck to N players hands
def dealHands(deck, players):
    players = players + 1
    hands = []
    #print(deck)
    random.seed(datetime.now())
    deck = random.sample(deck, len(deck))
    #print(deck)
    deckIndex = 0
    for player in range(1, players):
        hand = []
        for card in range(0, 5):
            #print(deckIndex)
            deltCard = deck[deckIndex]
            hand.append(deltCard)
            deckIndex = deckIndex + 1
        hands.append(hand)
    return hands

#Simulation Function
def runSimulation():
    
    #Set up statistics
    ranks_count = []
    ranks_wins = []
    for x in range(9): ranks_count.append(0)
    for x in range(9): ranks_wins.append(0)
    
    # Where n is the number of simulations
    deck = makeDeck()
    n = 500
    for x in range(n):
        # Deal random cards into 5 hands
        hands = dealHands(deck, 5)
        
        # The first hand is taken as the player hand
        playerHand = hands[0]
        currRank = findScore(playerHand)
        
        #Check if player has won the round
        win = True
        for opponent in range(1, len(hands)):
            if (betterHand(playerHand, opponent) == True):
                win = False
                break
                
        #Updates the statistics for the player rank
        ranks_count[currRank] = ranks_count[currRank] + 1
        if (win): ranks_wins[currRank] = ranks_wins[currRank] + 1
            
    return 0
    

    
runSimulation()


