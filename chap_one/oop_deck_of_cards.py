from random import shuffle


class Card:
    suites = ("Hearts", "Diamons", "Clubs", "Spades")
    values = ("A", "2 ", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suite, value):
        if value in Card.values:
            self.value = value
        if suite in Card.suites:
            self.suite = suite

    def __repr__(self):
        return f"{self.value} of {self.suite}"


class Deck:
    def __init__(self):
        self.cards = [Card(suite, value) for suite in Card.suites for value in Card.values]
        # make the all the possible cards:

        # for suite in Card.suites:
        #     for value in Card.values:
        #         self.cards.append(Card(suite, value))

    def __repr__(self):
        return f"{self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, hand_size):
        if self.count() == 0:
            raise ValueError("all the cards have been dealt")
        actual = min(hand_size, self.count())
        self.cards = self.cards[:-actual]
        return self.cards[-actual:]

    def deal_card(self):
        return self._deal(1)

    def shuffle(self):
        if self.count() != len(Card.values) * len(Card.suites):
            raise ValueError("the cards not full")
        return shuffle(self.cards)


deck1 = Deck()
print(deck1.shuffle())
print(deck1.cards, deck1.count(), deck1.deal_card())
