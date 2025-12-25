#!/usr/bin/env python3
import alchemy


def main():
    """
    __init__.py実装DEMO
    ・直接モジュールアクセス
    ・パッケージレベルアクセス
    この両方でテストしています。
    """

    print()
    print("=== Sacred Scroll Mastery ===")
    print()

    # 1.直接モジュールアクセス
    module_path = [alchemy.elements.create_fire,
                   alchemy.elements.create_water,
                   alchemy.elements.create_earth,
                   alchemy.elements.create_air]

    print("Testing direct module access:")
    for path in module_path:
        print(f"alchemy.elements.{path.__name__}(): {path()}")
    print()

    # 2.パッケージレベルアクセス
    print("Testing package-level access (controlled by __init__.py):")

    # 2-1.creat_fire()アクセス
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    except AttributeError as e:
        print(f"alchemy.create_fire(): {e}")

    # 2-2.creat_water()アクセス
    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except AttributeError as e:
        print(f"alchemy.create_water(): {e}")

    # 2-3.creat_earth()アクセス
    try:
        print(f"alchemy.create_eaarth(): {alchemy.create_eaarth()}")
    except AttributeError as e:
        print(f"alchemy.create_eaarth(): {e}")

    # 2-4.creat_air()アクセス
    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError as e:
        print(f"alchemy.create_air(): {e}")
    print()

    # 3.__init__.pyの詳細を出力
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}\n"
          f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
