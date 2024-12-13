class puzzle:

    def __init__(self):
        self.map = []
        self.guard_present = True
        self.guard_loc = []

    def parse_input(self):
        with open('test', 'r') as f:
            for line in f.readlines():
                self.map.append(list(line.replace("\n","")))
                
    def find_guard(self):
        col_idx = -1
        for row_idx,row in enumerate(self.map):
            try:
                col_idx = row.index("^")
                break
            except:
                pass
        
        if col_idx > 0:
            self.guard_loc = [row_idx,col_idx]
            self.guard_present = True
        else:
            self.guard_present = False
        return 
      
if __name__ == '__main__':
    p = puzzle()
    p.parse_input()
    # find current position of guard
    p.find_guard()
    
    # 