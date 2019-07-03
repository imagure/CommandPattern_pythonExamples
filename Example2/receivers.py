
class Sandwich:
    """
    The receiver class, which holds the specifc method to be called to
    perform the specific action.

    This will be called by the Invoker object.
    """

    def make_sandwich(self):
        print("A sandwich is being made")


class Salad:
    """
    The receiver class, which holds the specific method to be called.
    This will be called by the Invoker object.
    """

    def make_salad(self):
        print("A salad is being made")


class Taco:
    """
    The receiver class, which holds the specific method to be called.
    This will be called by the Invoker object.
    """

    def make_taco(self):
        print("A taco is being made")
