import FIFOStack
import random

class Game:
    def __init__(self):
        deck = self.shuffle_cards()
        deck1, deck2 = self.split_deck(deck)
        self.deck1 = Deck(FIFOStack.Stack.to_stack(deck1))
        self.deck2 = Deck(FIFOStack.Stack.to_stack(deck2))

    def play_game(self):
        while not (self.deck1.size() == 0 or self.deck2.size() == 0):
            card1 = self.deck1.get_next()
            card2 = self.deck2.get_next()
            if card1 > card2:
                self.deck1.give_card(card1)
                self.deck1.give_card(card2)
            elif card2 > card1:
                self.deck2.give_card(card1)
                self.deck2.give_card(card2)
            else:
                if self.deck1.size() >= 2 and self.deck2.size() >= 2:
                    self.war([card1], [card2])
                else:
                    break

        if self.deck1.size() < 2:
            print('Player 1 loses')
        elif self.deck2.size() < 2:
            print('Player 2 loses')

        

    
    def war(self, cards1, cards2):
        face_down_card1 = self.deck1.get_next()
        face_down_card2 = self.deck2.get_next()
        next_card1 = self.deck1.get_next()
        next_card2 = self.deck2.get_next()
        if next_card1 > next_card2:
            for card in  cards1:
                self.deck1.give_card(card)
            for card in  cards2:
                self.deck1.give_card(card)
            self.deck1.give_card(face_down_card1)
            self.deck1.give_card(face_down_card2)
            self.deck1.give_card(next_card1)
            self.deck1.give_card(next_card2)
        elif next_card2 > next_card1:
            for card in  cards1:
                self.deck2.give_card(card)
            for card in  cards2:
                self.deck2.give_card(card)
            self.deck2.give_card(face_down_card1)
            self.deck2.give_card(face_down_card2)
            self.deck2.give_card(next_card1)
            self.deck2.give_card(next_card2)
        else:
            cards1.append(face_down_card1)
            cards1.append(next_card1)
            cards2.append(face_down_card2)
            cards2.append(next_card2)
            self.war(cards1, cards2)




    def split_deck(self, deck):
        half = len(deck)//2
        return deck[:half], deck[half:]

    def shuffle_cards(self):
        cards = self.create_cards()
        deck = []
        while len(cards) != 0:
            idx = random.randint(0, len(cards) - 1)
            card = cards[idx]
            cards.remove(card)
            deck.append(card)
        return deck
        

    def create_cards(self):
        cards = []
        cards.append(Card('A'))
        cards.append(Card('A'))
        cards.append(Card('A'))
        cards.append(Card('A'))

        
        cards.append(Card('K'))
        cards.append(Card('K'))
        cards.append(Card('K'))
        cards.append(Card('K'))

        
        cards.append(Card('Q'))
        cards.append(Card('Q'))
        cards.append(Card('Q'))
        cards.append(Card('Q'))

        cards.append(Card('J'))
        cards.append(Card('J'))
        cards.append(Card('J'))
        cards.append(Card('J'))

        cards.append(Card(10))
        cards.append(Card(10))
        cards.append(Card(10))
        cards.append(Card(10))

        cards.append(Card(9))
        cards.append(Card(9))
        cards.append(Card(9))
        cards.append(Card(9))

        cards.append(Card(8))
        cards.append(Card(8))
        cards.append(Card(8))
        cards.append(Card(8))

        cards.append(Card(7))
        cards.append(Card(7))
        cards.append(Card(7))
        cards.append(Card(7))

        cards.append(Card(6))
        cards.append(Card(6))
        cards.append(Card(6))
        cards.append(Card(6))

        cards.append(Card(5))
        cards.append(Card(5))
        cards.append(Card(5))
        cards.append(Card(5))

        cards.append(Card(4))
        cards.append(Card(4))
        cards.append(Card(4))
        cards.append(Card(4))

        cards.append(Card(3))
        cards.append(Card(3))
        cards.append(Card(3))
        cards.append(Card(3))

        cards.append(Card(2))
        cards.append(Card(2))
        cards.append(Card(2))
        cards.append(Card(2))

        return cards

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def get_next(self):
        return self.cards.pop()

    def give_card(self, card):
        self.cards.push(card)

    def size(self):
        return self.cards.size()

class Card:
    def __init__(self, card):
        self.num = self.get_num(card)

    def get_num(self, card):
        if card == 'A':
            num = 14
        elif card == 'K':
            num = 13
        elif card == 'Q':
            num = 12
        elif card == 'J':
            num = 11
        else:
            num = card
        return num
        
    def __gt__(self, other):
        return self.num > other.num

    def __ge__(self, other):
        return self.num >= other.num

    def __lt__(self, other):
        return self.num < other.num
    
    def __le__(self, other):
        return self.num <= other.num

    def __ne__(self, other):
        return self.num != other.num

    def __eq__(self, other):
        return self.num == other.num

#game = Game()
#game.play_game()
#print('a')