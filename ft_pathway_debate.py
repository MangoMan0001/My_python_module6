#!/usr/bin/env python3

def main() -> None:
    """
    絶対パスと相対パスの違いDEMO
    """

    print()
    print("=== Pathway Debate Mastery ===")
    print()

    # 1.Testing絶対パス
    print("Testing Absolute Imports (from basic.py):")
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print(f"lead_to_gold(): {lead_to_gold()}\n"
          f"stone_to_gem(): {stone_to_gem()}")
    print()

    # 2.Testing相対パス
    print("Testing Relative Imports (from advanced.py):")
    from alchemy.transmutation import philosophers_stone, elixir_of_life
    print(f"philosophers_stone():{philosophers_stone()}\n"
          f"elixir_of_life(): {elixir_of_life()}")
    print()

    # 3.Testing Package Access:
    print("Testing Package Access:")
    print(f"alchemy.transmutation.lead_to_gold():{lead_to_gold()}\n"
          "alchemy.transmutation.philosophers_stone(): "
          f"{philosophers_stone()}")
    print()

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":

    main()
