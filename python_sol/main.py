"""
Docstring for main
"""

# TODO: verbosity
# TODO: comments

def run_game(num_disks: int) -> None:
    opt_moves_count = 2**num_disks - 1
    moves_count = 0
    towers = [[i for i in range(1, num_disks+1)], [], []]
    # print(f"opt moves: {opt_moves_count}")
    # print_towers(num_disks, towers)

def print_towers(num_disks: int, towers: list) -> None:
    len_padding = num_disks + 2
    tower_char = "|"
    with open("output.txt", "w") as f:
        f.write(((tower_char.center(len_padding*2 + 1, " "))*3 + "\n")*(num_disks))
        for i in range(1, num_disks+1):
            s = ""
            for tower in towers:
                disk = "|"
                if i in tower:
                    disk = "[" + ("_" * (i-1)) + str(i) + ("_" * (i-1)) + "]"
                disk = disk.center(len_padding*2 + 1, " ")
                s = s + disk
            f.write(s + "\n")

def main():
    num_disks = 3
    run_game(num_disks)

if __name__ == "__main__":
    main()