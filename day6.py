import copy 

class puzzle:

    def __init__(self):
        self.map = []
        self.map_size = []
        self.row_idx = []
        self.col_idx = []
        self.guard_past_positions = []
        self.direction = 0
        self.unique_locs = []
        self.new_obstacles = []

    def parse_input(self):
        self.map=[]
        with open("inputs/input_d6", "r") as f:
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
            # print(counter)

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
            # print(
            #     # f"Direction is: {self.direction}. Advancing from [{self.row_idx},{self.col_idx}] to [{row},{col}]"
            # )
            self.row_idx = row
            self.col_idx = col
            self.guard_past_positions.append([self.row_idx, self.col_idx])

        else:
            self.direction = (self.direction + 1) % 4
            # print(f"Obstacle reached: {next_tile}. New direction is: {self.direction}")

            # we broke out of the map

        return

    def calc_unique_locs(self):
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
                    new_list.append(m)
                    
        self.unique_locs = new_list
        
        
    def calc_new_obstacle(self):
        max_count = 25000
        obstacle_list = []
        # reinit values
        og_map = copy.deepcopy(self.map)
        
        
        
        # loop through all positions and see if it impacts path traveled
        # new_count = 0
        for idx,u in enumerate(self.unique_locs):
            r = u[0]
            c = u[1]
            
            # if self.map[r][c] == "#":
            #     continue
            self.map = copy.deepcopy(og_map)
            self.init_guard()
            self.map[r][c] = "#"        
            counter = 0
            flag_loop = False
            # new_count += 1
            # if new_count > 1000:
            #     break
            
            if idx % 100 == 0:
                print(f"Iter: {idx}/{len(self.unique_locs)}. {len(obstacle_list)} obstacles found.")
                
            while self.row_idx in range(0, self.map_size[0]) and self.col_idx in range(
                0, self.map_size[1]
            ):
                self.next_step()
                counter += 1
                # print(counter)

                if counter >= max_count:
                    obstacle_list.append([r,c])
                    # print(f"Obstacle at: {r}|{c}. Counter reached: {counter}")
                    break
                
            # print(f"Obstacle at: {r}|{c}. Counter reached: {counter}")
            
        
        self.new_obstacles = obstacle_list
        return
                

if __name__ == "__main__":
    p = puzzle()
    p.parse_input()
    # find current position of guard
    p.init_guard()

    p.guard_logic()
    p.calc_unique_locs()

    print(f"Guard will travel to {len(p.unique_locs)} different positions.")
    # print(p.unique_locs)
    
    p.calc_new_obstacle()
    print(f"We can place {len(p.new_obstacles)} new obstacles.")

    #
