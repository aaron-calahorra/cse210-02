import constants
from game.casting.actor import Actor
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        
    def start_game(self, cast, script):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        snake = cast.get_first_actor("snakes")
        snake2 = cast.get_second_actor("snakes")
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(cast, script) 
        if not constants.GAME_OVER:
            snake.grow_tail(1, constants.GREEN)
            snake2.grow_tail(1, constants.RED)
        # NUMBER_OF_FRAMES +=1
        # if NUMBER_OF_FRAMES == 45:
        #         NUMBER_OF_FRAMES = 0         