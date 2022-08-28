from random import shuffle


# useful variables to creating cards
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#my_cards = [(s,r) for s in SUITE  for r in RANKS]     this we can also do but i will go with nested for loops

"""mycards = []
for r in RANKS:
    for s in SUITE:
        mycards.append((s,r))"""

class Deck():
    
    #it will create a deck of cards to play
    
    def __init__(self):
        print("Creating new ordered deck of cards:- ")
        self.allcards = [(s,r) for s in SUITE  for r in RANKS]
        
        
    def shuffle(self):
        print("The decks are shuffling:-")
        shuffle(self.allcards)
        
    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])
    
    
class Hand():
    
 #this is hand class. Every player will ahave a hand and they can add or remove cards from their hand   
    
    def __init__(self,cards):
        self.cards = cards
    
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))
    
    
    def add(self,added_cards):
        self.cards.extend(added_cards)
        
    def remove_cards(self):
        return self.cards.pop()
    

class Player():


# In this class player will take a name and an instant of a hand class object...
# Player can play cards and also can check that they still have a cards or not.

    def __init__(self,name,hand):
        self.name = name
        self .hand = hand
        
    def play_card(self):
        drawn_cards = self.hand.remove_cards()
        print("{} has take placed: {}".format(self.name,drawn_cards))
        print("\n")
        return drawn_cards
    
    
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
    
    def still_has_cards(self):
        return len(self.hand.cards) != 0
    
    
    
print("Welcome to War, let's begin...")



#create new deck object

d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()


#create both player!

comp = Player("computer",Hand(half1))

name = input('What is your name? :-')
user = Player(name,Hand(half2))


total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for new round :-")
    print("Here are the Current standing :-")
    print(user.name+"has the count :"+str(len(user.hand.cards)))
    print(comp.name+"has the count :"+str(len(comp.hand.cards)))
    print("Play a card:-")
    print('\n')
    
    
    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()
    
    
    table_cards.append(c_card)
    table_cards.append(p_card)
    
    if c_card[1] == p_card[1]:
        war_count += 1
        
        print("War!")
        
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
            
            
print("Game over, number of rounds:"+str(total_rounds))
print("A war happened "+str(war_count)+" times..")
print("Does the Computer still have cards?")
print(str(comp.still_has_cards()))
print("Does the Human still have cards?")
print(str(user.still_has_cards()))
    
    
    
    