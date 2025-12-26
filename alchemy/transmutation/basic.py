#!/usr/bin/env python3
from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """
    鉛が金になります(まさかの)
    """

    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """
    石が宝石になります(誰でも磨けば宝石になれる)
    """

    return f"Stone transmuted to gem using {create_earth()}"


if __name__ == "__main__":
    pass
