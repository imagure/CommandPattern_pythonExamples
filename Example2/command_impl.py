from command_interface import Command
from receivers import *

class SandwichCommand(Command):
    """
    A concrete / specific Command class, implementing exectue()
    which calls a specific or an appropriate action of a method
    from a Receiver class.

    Args:
        lunch (Lunch): Receiver class to be attached to the command
    """

    def __init__(self, sandwich: Sandwich):
        self._sandwich = sandwich

    def execute(self):
        self._sandwich.make_sandwich()


class SaladCommand(Command):
    def __init__(self, salad: Salad):
        self._salad = salad

    def execute(self):
        self._salad.make_salad()


class TacoCommand(Command):
    def __init__(self, taco: Taco):
        self._taco = taco

    def execute(self):
        self._taco.make_taco()