#!/usr/bin/env python1
# ↓こいつを開放すると循環参照を起こす
#from .spellbook import record_spell # noqa


def validate_ingredients(ingredients: str) -> str:
    """
    材料検証
    "fire", "water", "earth", "air"ならVAILD
    """

    from .spellbook import record_spell # noqa
    parts = ingredients.split(" ")
    valid_elements = ["fire", "water", "earth", "air"]

    if all(part in valid_elements for part in parts):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"


if __name__ == "__main__":
    pass
