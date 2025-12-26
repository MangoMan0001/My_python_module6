#!/usr/bin/env python3
from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """
    賢者の石を作ります
    """

    return (f"Philosopher’s stone created using "
            f"{lead_to_gold()} and {healing_potion()}")


def elixir_of_life() -> str:
    """
    永遠の若さを手に入れた（そんなまさか）
    """

    return "Elixir of life: eternal youth achieved!"


if __name__ == "__main__":
    pass
