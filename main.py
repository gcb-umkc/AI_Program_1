import csv
import random 
from datetime import datetime
from pprint import pprint
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

def nameScore(score):
    if(score == 0): return "No pair"
    if(score == 1): return "One pair"
    if(score == 2): return "Two pair"
    if(score == 3): return "Three of a kind"
    if(score == 4): return "Straight"
    if(score == 5): return "Flush"
    if(score == 6): return "Full House"
    if(score == 7): return "Four of a kind"
    if(score == 8): return "Straight Flush"
    if(score == 9): return "Royal Flush"

#Simulation Function
def runSimulation():
    
    #Set up statistics
    ranks_count = []
    ranks_wins = []
    ranks_percentage = []
    ranks_wpercentage = []
    labels = []
    
    for x in range(10): 
        ranks_count.append(0)
        ranks_wins.append(0)
        ranks_percentage.append(0)
        ranks_wpercentage.append(0)
        labels.append("")
        
    file = open('results.csv', mode='w', newline='')
    resultWriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Where n is the number of simulations
    deck = makeDeck()
    n = 100000
    for x in range(n):
        # Deal random cards into 5 hands
        hands = dealHands(deck, 5)
        
        # The first hand is taken as the player hand
        playerHand = hands[0]
        currRank = findScore(playerHand)
        
        #Check if player has won the round
        win = True
        for opponent in range(1, len(hands)):
            if (betterHand(playerHand, hands[opponent]) == True):
                win = False
                break
                
        #Updates the statistics for the player rank
        ranks_count[currRank] = ranks_count[currRank] + 1
        if (win): ranks_wins[currRank] = ranks_wins[currRank] + 1
        hands.append(nameScore(currRank))
        hands.append(win)
        resultWriter.writerow(hands)
    
    for x in range(10): 
        ranks_percentage[x] = ranks_count[x] / float(n)
        ranks_wpercentage[x] = ranks_wins[x] / float(n)
        labels[x] = nameScore(x)
    
    print(labels)
    pprint("Rank #")
    pprint(ranks_count)
    pprint("Wins")
    pprint(ranks_wins)
    pprint("Rank Percentages")
    pprint(ranks_percentage)
    pprint("Win Percentages")
    pprint(ranks_wpercentage)
    file.close()

runSimulation()


