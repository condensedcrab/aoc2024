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
            self.guard_past_positions.append([row_idx,col_idx])
        return

    def guard_logic(self):

        for i in range(0, 10):
            self.next_step()
            
    def next_step(self):
        
        if direction == 0: # up
            self.row_idx -= 1
        elif direction == 1: # right
            self.col_idx += 1
        elif direction == 2: # down
            self.row_idx += 1
        elif direction == 3: # left
            self.col_idx -= 1
        else:
            raise ValueError # should be unreachable
        
        next_tile = map[row_idx][col_idx]
        if next_tile == "." | next_tile == "^":
              
        else:
            direction = direction+1 % 4
            self.next_step()
            
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
