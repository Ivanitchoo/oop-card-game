import random

suits = ('Hearts','Diamonds','Spades','Clubs')

ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card():
   

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self) -> str:
        return self.rank + " Of " + self.suit
    
############################# Split - Deck Class ###########################################

class Deck():

    #create the 52 cards
    def __init__(self):
        
        self.all_cards = []

        # for each suit, I have to create a rank. E.g: 2, 3,4,... Hearts; 2,3,4,... Clubs; etc
        for suit in suits:
            for rank in ranks:
                #create the card object.
                created_card = Card(suit,rank)
                
                
                self.all_cards.append(created_card) #through this loop at the end I will a ve a stack of unique cards
              
    #shuffle the cards              
    def shuffle(self): #shuffle the list of cards
        random.shuffle(self.all_cards)

    #remove one card from the deck
    def deal_one(self):
        return self.all_cards.pop()
        

############################# Split - Player Class ###########################################

class Player():

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) ==type([]):
            #this if we have a list of new cards
            self.all_cards.extend(new_cards)
        else:
            #this if we have a single new card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

'''
new_player = Player("Ivan")

deck_of_cards = Deck ()
deck_of_cards.shuffle()
mycard = deck_of_cards.deal_one()

new_player.add_cards(mycard)


print(new_player)
print(new_player.all_cards[0])

new_player.add_cards([mycard,mycard,mycard, mycard, mycard])
print(new_player)

new_player.remove_one()
print(new_player)
'''


############################# Split - Game Logic ###########################################

#Game Setup
player_one = Player("Abel")
player_two = Player("Ivan")

new_deck = Deck()
new_deck.shuffle()

#split the deck between both players (A full deck has 52 cards)
for x in range (26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
#print (player_two.all_cards[0])


while game_on:
    round_num += 1
    print("Round {}".format(round_num))

    if len(player_one.all_cards)==0:
        print("Player 2 Wins bc Player 1 is out of cards.")
        game_on = False
        break

    if len(player_two.all_cards)==0:
        print("Player 1 Wins bc Player 2 is out of cards.")
        game_on = False
        break    

    # START A NEW ROUND
    #player one and two grabs a single card
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    #WHILE AT WAR
    #CHECK THE PLAYERS CARDS AGAINST EACH OTHER

    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print ("Player One unable to declare war")
                print ("PLAYER TWO WINS")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print ("Player Two unable to declare war")
                print ("PLAYER ONE WINS")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())