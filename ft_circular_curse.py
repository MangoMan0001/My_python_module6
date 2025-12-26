#!/usr/bin/env python3
from alchemy.grimoire import validate_ingredients, record_spell


def main() -> None:
    """
    デッドロック解消DEMO
    """

    print()
    print("=== Circular Curse Breaking ===")
    print()

    # 1.材料検証
    print("Testing ingredient validation:")
    test_ingredients = ["fire air", "dragon scales"]
    for case in test_ingredients:
        print(f'validate_ingredients({case}): {validate_ingredients(case)}')
    print()

    # 2.呪文検証
    print("Testing spell recording with validation:")
    test_ingredients = ["fire air", "shadow"]
    test_spell = ["Fireball", "Dark Magic"]
    for spell, ingredients in zip(test_spell, test_ingredients):
        print(f"record_spell({spell}, {ingredients}): "
              f"Spell recorded: {record_spell(spell, ingredients)}")
    print()

    # 3.デッドロック解消DEMO(?)
    print("Testing late import technique:")
    print('record_spell("Lightning", "air"): '
          f'Spell recorded: {record_spell("Lightnig", "air")}')
    print()

    print("Circular dependency curse avoided using late imports!\n"
          "All spells processed safely!")


if __name__ == "__main__":
    main()
