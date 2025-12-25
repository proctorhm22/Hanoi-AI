"""
Docstring for main

Assumes three towers

Game won when all stacked in tower three
"""

# TODO: verbosity / error handling

from hanoi import Hanoi

def run_game(num_disks: int) -> None:
    try:
        h = Hanoi(num_disks)
        # print(h)
        # print(get_tower_max(h, 1))
        # print(get_tower_max(h, 2))
        # print(get_tower_max(h, 3))

        # h.swap(1, 2)
        # print(h)
        # print(get_tower_max(h, 1))
        # print(get_tower_max(h, 2))
        # print(get_tower_max(h, 3))

        # h.swap(1, 3)
        # print(h)
        # print(get_tower_max(h, 1))
        # print(get_tower_max(h, 2))
        # print(get_tower_max(h, 3))

        # h.swap(2, 3)
        # print(h)
        # print(get_tower_max(h, 1))
        # print(get_tower_max(h, 2))
        # print(get_tower_max(h, 3))

        # h.swap(1, 2)
        # print(h)
        # print(get_tower_max(h, 1))
        # print(get_tower_max(h, 2))
        # print(get_tower_max(h, 3))

        # h.swap(2, 3)
        # print(h)
    except Exception as e:
        print(e)

def next_count(h: Hanoi):
    """
    Go down tower 1
    """
    pass

def get_tower_max(h: Hanoi, i: int):
    """
    Return max disk in tower_i
    """
    if i < 1 or i > h.NUM_TOWERS:
        raise ValueError(f"ERROR: invalid i -- {i} (must be between 1 and {h.NUM_TOWERS})")
    return max(h.towers[i-1], default=-1)

def main():
    num_disks = 3
    run_game(num_disks)

if __name__ == "__main__":
    main()