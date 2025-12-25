"""
Docstring for python_sol.classes
"""

# TODO: error handling

class Hanoi():

    NUM_TOWERS = 3

    def __init__(self, num_disks):
        """
        Create a new game
        """
        if num_disks < 0:
            raise ValueError(f"ERROR: invalid number of disks -- {num_disks} (must be > 0)")
        self.num_disks = num_disks
        self.opt_moves_count = 2**num_disks - 1
        self.moves_count = 0
        self.towers = [[i for i in range(1, num_disks+1)]]
        for i in range(0, self.NUM_TOWERS - 1):
            self.towers.append([])

    def swap(self, i, j):
        """
        Swap disk from tower_i to tower_j
        """
        if i < 1 or i > self.NUM_TOWERS:
            raise ValueError(f"ERROR: invalid i -- {i} (must be 1, 2, or 3)")
        if j < 1 or j > self.NUM_TOWERS:
            raise ValueError(f"ERROR: invalid j -- {j} (must be 1, 2, or 3)")
        disk = min(self.towers[i-1], default=-1)
        if disk == -1:
            raise ValueError(f"ERROR: no disks in tower_{i} (cannot move disks that don't exist)")
        if disk < min(self.towers[j-1], default=self.num_disks+1):
            self.towers[i-1].remove(disk)
            self.towers[j-1].append(disk)
        else:
            raise ValueError("ERROR: CANNOT PUT LARGER DISKS ON TOP OF SMALLER DISKS "
                             + f"(cannot swap from tower {i} to tower {j} -- {disk} >= {min(self.towers[j-1], default=self.num_disks+1)})")

    def __str__(self):
        """
        "Print" current state of the game
        """
        len_padding = self.num_disks + 2
        tower_char = "|"
        towers = [tower.copy() for tower in self.towers]
        lengths = [len(tower) for tower in self.towers]
        final_str = ""
        while any(l > 0 for l in lengths):
            s = ""
            for i in range(0, self.NUM_TOWERS):
                disk = tower_char
                if len(towers[i]) > 0:
                    max_val = max(towers[i])
                    towers[i].remove(max_val)
                    disk = "[" + ("_" * (max_val-1)) + str(max_val) + ("_" * (max_val-1)) + "]"
                    lengths[i] = lengths[i] - 1
                disk = disk.center(len_padding*2 + 1, " ")
                s = s + disk
            final_str = s + "\n" + final_str
        final_str = "\n" + ((tower_char.center(len_padding*2 + 1, " "))*3 + "\n")*(self.num_disks) + final_str
        return final_str