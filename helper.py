# Evaluation Function
# Ranks are represented from 


def findCount(hand):
    count = []
    for card in range(13):
        count.append(0)
        
    for card in hand:
        card = card[0] - 1
        count[card] = count[card] + 1
    return count

def findnKind(n, hand):
    count = findCount(hand)
    
    #Checks for that n-th flush and n-th flush only
    for card in count:
        if (card == n):
            return True
    return False

def compareNoPair(player, opponent):
    for index in reversed(range(len(player))):
        if (player[index] > opponent[index]):
            return True
        else:
            pass
    return False

def arrayPair(hand, num):
    count = findCount(hand)
    remHand = hand
    playerPairs = []
    for rank in range(len(count)):
        if (count[rank] == num):
            for card in hand:
                if (card[0] == rank + 1):
                    playerPairs.append(card)
                    hand.remove(card)
    #print(playerPairs)
    return playerPairs, remHand

def compareOnePair(player, opponent):

    playerPairs, tempPlayer = arrayPair(player, 2)
    opponentPairs, tempOpponent = arrayPair(opponent, 2)
    
    if (playerPairs[0] > opponentPairs[0]):
        return True
    else:
        return compareNoPair(player, opponent)
    
def findTwoPair(hand):
    count = []
    for card in range(13):
        count.append(0)
        
    for card in hand:
        card = card[0] -1
        count[card] = count[card] + 1
    
    #print(count)
    #Checks for that n-th flush and n-th flush only
    pairs = 0
    for card in count:
        if (card == 2):
            pairs = pairs + 1
    if(pairs == 2): return True
    else: return False

def comparePairs(player, opponent, num):
    playerPairs, tempPlayer = arrayPair(player, num)
    opponentPairs, tempOpponent = arrayPair(opponent, num)
    
    if(compareNoPair(playerPairs, opponentPairs) == False):
        return compareNoPair(tempPlayer, tempOpponent)
        
    return True
    
def compareThreeKind(player, opponent):    
    return comparePairs(player, opponent, 3)
    
def compareTwoPair(player, opponent):
    return comparePairs(player, opponent, 2)

def compareFourPair(player, opponent):  
    return comparePairs(player, opponent, 4)

def findStraight(hand):
    for index in range(len(hand) - 1):
        if (hand[index][0] != (hand[index + 1][0] - 1)):
            return False
    return True

def compareStraight(player, opponent):
    if(max(player)[0] > max(opponent)[0]):
        return True
    else:
        return False
    
def findFlush(hand):
    for index in range(len(hand) - 1):
        if (hand[index][1] != (hand[index + 1][1])):  
            return False
    return True

def compareFlush(player, opponent):
    return compareNoPair(player, opponent)
    
def fullHouse(hand):
    if(findnKind(2, hand) & findnKind(3, hand)):
        return True
    else:
        return False
    
def compareFullHouse(player, opponent):
    return compareThreeKind(player, opponent)

def straightFlush(hand):
    if(findFlush(hand) & findStraight(hand)):
        return True
    else:
        return False
    
def compareStraightFlush(player, opponent):
    return compareFlush(player, opponent)

def royalFlush(hand):
    if(findFlush(hand) == False):
        return False
    royal = [(1, 1), (10, 1), (11, 1), (12, 1), (13, 1)]
    hand.sort()
    for index in range(len(royal) - 1):
        if (royal[index][0] != hand[index][0]):
            return False
    return True
    
def findScore(hand):
    
    score = -1
    if(findnKind(1, hand)): score = 0
    if(findnKind(2, hand)): score = 1
    
    if(findTwoPair(hand)): score = 2
    
    if(findnKind(3, hand)): score = 3
    
    if(findStraight(hand)): score = 4
    
    if(findFlush(hand)): score = 5
    
    if(fullHouse(hand)): score = 6
    if(findnKind(4, hand)): score = 7
    
    if(straightFlush(hand)): score = 8
    if(royalFlush(hand)): score = 9
    
    if(score == -1):
        raise BaseException
    return score
    
test_hand = [(11, 1), (1, 1), (13, 1), (12, 1), (10, 1)]
test_opponent = [(1, 2), (2, 3), (3, 1), (4, 1), (5, 1)]

    
#print (findScore(test_hand))
#print (findScore(test_opponent))

#Tiebreakers!
def compareHands(player, opponent):
    player.sort()
    opponent.sort()
    score = findScore(player)
    #print(score)
    
    if (score == 0):
       return compareNoPair(player, opponent)
    if (score == 1):
        return compareOnePair(player, opponent)
    if (score == 2):
        return compareTwoPair(player, opponent)
    if (score == 3):
        return compareThreeKind(player, opponent)
    if (score == 4):
        return compareStraight(player, opponent)
    if (score == 5):
        return compareFlush(player, opponent)
    if (score == 6):
        return compareFullHouse(player, opponent)
    if (score == 7):
        return compareFourPair(player, opponent)
    if (score == 8):
        return compareStraightFlush(player, opponent)
    if (score == 9):
        raise BaseException

#Finds the better of 2 hands
def betterHand(player, opponent):
    if(findScore(player) > findScore(opponent)):
        return True
    
    if(findScore(player) < findScore(opponent)):
        return False
    
    #Need to break ties
    if(findScore(player) == findScore(opponent)):
        return compareHands(player, opponent)
    