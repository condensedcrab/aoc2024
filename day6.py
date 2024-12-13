class puzzle:

    def __init__(self):
        self.map = []
        self.guard_loc = []
        self.guard_positions = []

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
            self.guard_loc = [row_idx, col_idx]

        return

    def guard_logic(self):
        # initialize state
        row_idx = self.guard_loc[0]
        col_idx = self.guard_loc[1]
        direction = "up"

        for i in range(0, 10):
            row_idx, col_idx, direction = self.next_step(
                self.map, row_idx, col_idx, direction
            )

    def next_step(map, row_idx, col_idx, direction):

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
