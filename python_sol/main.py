"""
Docstring for main
"""

# TODO: verbosity

from hanoi import Hanoi

def run_game(num_disks: int) -> None:
    try:
        h = Hanoi(num_disks)
        print(h)
        h.swap(1, 2)
        print(h)
        h.swap(1, 3)
        print(h)
        h.swap(2, 3)
        print(h)
        h.swap(1, 2)
        print(h)
        h.swap(2, 3)
        print(h)
    except Exception as e:
        print(e)

def main():
    num_disks = 3
    run_game(num_disks)

if __name__ == "__main__":
    main()