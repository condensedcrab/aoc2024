class puzzle:

    def __init__(self):
        self.map = []
        self.guard_loc = []

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


if __name__ == "__main__":
    p = puzzle()
    p.parse_input()
    # find current position of guard
    p.find_guard()

    #
