"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int):
    """Calculate time to prepare lasagna.

    Parameters:
        number_of_layers (int): How many layers in lasagna.

    Returns:
        int: Time if takes to prepare the lasagna (in minutes) if each layer takes 2 minutes

    Function that takes the amount of layers in the lasagna, multiplies that by the 'PREPARATION_TIME' constant,
    returning the number of minutes it will take to prepare the lasgna before cooking.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate time it will take to cook (preparation time / cooking time inclusive)

    Parameters:
        number_of_layers (int): How many layers in lasgna.
        elapsed_bake_time (int): Number of minutes lasagna has already spent baking.

    Returns:
        int: How long has it taken to cook so far (Including preparation time)

    Function that takes the number of layers and elapsed baking time so far
    and calculates how long (Including preparation) it has taken to cook
    """
    return (number_of_layers * PREPARATION_TIME) + elapsed_bake_time
