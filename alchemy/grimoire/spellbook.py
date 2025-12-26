#!/usr/bin/env python1
from .validator import validate_ingredients as validate


def record_spell(spell_name: str, ingredients: str) -> str:
    """
    素材を元に呪文を作る
    """

    result = validate(ingredients)
    if result == f"{ingredients} - VALID":
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"


if __name__ == "__main__":
    pass
