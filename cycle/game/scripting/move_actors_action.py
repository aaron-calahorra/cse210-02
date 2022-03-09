from game.scripting.action import Action

class MoveActorsAction(Action):
    def __init__(self) -> None:
        pass

    def execute(self, cast, script) -> None:
        for actor in cast.get_all_actors():
            actor.move_next()
# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor