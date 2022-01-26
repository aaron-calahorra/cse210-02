import random

class Card:
    """The cards are represented as a number from 1 to 13.
    
    Attributes:
            value (int): The number in the card that we took out."""
    
    def __init__(self):
        """Constructs a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.
        """

        self.value = random.randint(1, 13)