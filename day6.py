class puzzle:

    def __init__(self):
        self.map = []
        self.map_size = [len(self.map), len(self.map[0])]
        self.row_idx = []
        self.col_idx = []
        self.guard_past_positions = []
        self.direction = 0

    def parse_input(self):
        with open("test", "r") as f:
            for line in f.readlines():
                self.map.append(list(line.replace("\n", "")))

    def init_guard(self):
        col_idx = -1
        for row_idx, row in enumerate(self.map):
            try:
                col_idx = row.index("^")
                break
            except:
                pass

        if col_idx > 0:
            self.row_idx = row_idx
            self.col_idx = col_idx
            self.guard_past_positions.append([row_idx, col_idx])
        return

    def guard_logic(self):

        while self.row_idx in range(0,self.map_size[0]) and self.col_idx in range(0,self.map_size[1]):
            

    def next_step(self):

        row = self.row_idx
        col = self.col_idx

        # find next position
        if direction == 0:  # up
            row -= 1
        elif direction == 1:  # right
            col = 1
        elif direction == 2:  # down
            row += 1
        elif direction == 3:  # left
            col -= 1
        else:
            raise ValueError  # should be unreachable

        next_tile = map[row][col]

        # determine if we continue or change directions
        if next_tile == "." | next_tile == "^":
            self.row_idx = row
            self.col_idx = col
        else:
            direction = direction + 1 % 4
        return

        # move in direction


if __name__ == "__main__":
    p = puzzle()
    p.parse_input()
    # find current position of guard
    p.init_guard()

    p.guard_logic()

    print(f"Guard will travel to {len(self.guard_positions)} different positions.")

    #
