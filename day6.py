class puzzle:

    def __init__(self):
        self.map = []
        self.map_size = []
        self.row_idx = []
        self.col_idx = []
        self.guard_past_positions = []
        self.direction = 0
        self.unique_locs = 0

    def parse_input(self):
        with open("test", "r") as f:
            for line in f.readlines():
                self.map.append(list(line.replace("\n", "")))

        self.map_size = [len(self.map), len(self.map[0])]

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
            self.guard_past_positions.append([self.row_idx, self.col_idx])
        return

    def guard_logic(self):
      
        counter = 0
        while self.row_idx in range(0, self.map_size[0]) and self.col_idx in range(
            0, self.map_size[1]
        ):
            self.next_step()
            counter += 1
            print(counter)

    def next_step(self):
        flag_within_map = True
        row = self.row_idx
        col = self.col_idx

        # find next position
        if self.direction == 0:  # up
            row -= 1
        elif self.direction == 1:  # right
            col += 1
        elif self.direction == 2:  # down
            row += 1
        elif self.direction == 3:  # left
            col -= 1
        else:
            raise ValueError  # should be unreachable

        try:
            next_tile = self.map[row][col]
        except:
            next_tile = "escape"

        # determine if we continue or change directions
        if next_tile == "escape":
            self.row_idx = row
            self.col_idx = col
        if next_tile == "." or next_tile == "^":
            print(
                f"Direction is: {self.direction}. Advancing from [{self.row_idx},{self.col_idx}] to [{row},{col}]"
            )
            self.row_idx = row
            self.col_idx = col
            self.guard_past_positions.append([self.row_idx, self.col_idx])

        else:
            self.direction = (self.direction + 1) % 4
            print(f"Obstacle reached: {next_tile}. New direction is: {self.direction}")

            # we broke out of the map

        return

    def unique_locs(self):
        new_list = []
        
        for m in self.guard_past_positions:
            if not new_list:
                new_list.append(m)
            else:
                flag_found = False
                for n in new_list:
                    if m == n:
                        flag_found = True
                
                if flag_found is False:
                    new_list.append(n)
                

if __name__ == "__main__":
    p = puzzle()
    p.parse_input()
    # find current position of guard
    p.init_guard()

    p.guard_logic()

    print(f"Guard will travel to {p.unique_locs} different positions.")

    #
