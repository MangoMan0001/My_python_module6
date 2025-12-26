#!/usr/bin/env python3

def main() -> None:
    """
    様々なインポート種類をDEMOする
    """

    print()
    print("=== Import Transmutation Mastery ===")
    print()

    # 1.ノーマルインポート
    import alchemy.elements
    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print()

    # 2.特定のインポート
    from alchemy.elements import create_fire
    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_fire()}")
    print()

    # 3.別名付きインポート
    from alchemy.potions import healing_potion as heal
    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")
    print()

    # 4.複数インポート
    from alchemy import elements, potions
    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {elements.create_earth()}\n"
          f"create_fire(): {elements.create_fire()}\n"
          f"strength_potion(): {potions.strength_potion()}")
    print()

    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
