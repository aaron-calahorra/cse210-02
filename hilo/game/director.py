from game.card import Card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        deck (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 0
        self.total_score = 300

        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        
        
        current_card = Card()
        
        while self.is_playing:
            print(f"\nThe card is: {current_card.value}")
            guess = input("Higher or lower? (h/l) ").lower()
            next_card = Card()
            print(f"Next card is {next_card.value}")

            if guess == "h":
                if current_card.value < next_card.value:
                    self.score = 100
                else:
                    self.score = -75
            elif guess == "l":
                if current_card.value > next_card.value:
                    self.score = 100
                else:
                    self.score = -75
            
            self.total_score += self.score
            print(f"Your score is: {self.total_score}")

            if self.total_score > 0:
                next_round = input("Play again? (y/n) ").lower()
                self.is_playing = (next_round == "y")
                current_card = next_card
            else:
                self.is_playing = False
        
        print("Game over")