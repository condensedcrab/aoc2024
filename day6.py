class puzzle:

    def __init__(self):
        self.map = []
        self.row_idx= []
        self.col_idx = []
        self.guard_past_positions = []
        self.direction = 0

    def parse_input(self):
        with open("test", "r") as f:
            for line in f.readlines():
                self.map.append(list(line.replace("\n", "")))

    def find_guard_start(self):
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

        return

    def guard_logic(self):

        for i in range(0, 10):
            self.next_step()
            
    def next_step(self):
        
        if direction == 0: # up
            row_idx -= 1
        elif direction == 1: # right
            col_idx += 1
        elif direction == 2: # down
            row_idx += 1
        elif direction == 3: # left
            col_idx -= 1
        else:
            raise ValueError # should be unreachable
        
        next_tile = map[row_idx][col_idx]
        if next_tile == "." | next_tile == "^":
        
        else:
            direction 
        return row_idx, col_idx, direction

        # move in direction


if __name__ == "__main__":
    p = puzzle()
    p.parse_input()
    # find current position of guard
    p.find_guard_start()

    p.guard_logic()

    print(f"Guard will travel to {len(self.guard_positions)} different positions.")

    #
