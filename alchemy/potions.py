#!/usr/bin/env python3
from .elements import create_fire, create_water, create_air, create_earth


def healing_potion() -> str:
    """
    回復するポーションを作る
    """

    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    """
    力が出るポーションを作る(引っ越しに便利！！)
    """

    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    """
    透明になれるポーションを作る(悪用厳禁！)
    """

    return f"Invisibility potion brewed with {create_air()} and {create_water()}"


def wisdom_potion() -> str:
    """
    賢くなるポーションを作る(とても欲しい)
    """

    all_four_results = (f"{create_fire()}, {create_water()}, "
                        f"{create_earth()}, {create_air()}")
    return f"Wisdom potion brewed with all elements: {all_four_results}"
