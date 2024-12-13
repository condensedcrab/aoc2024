class puzzle:

    def __init__(self):
        self.input = []

    def parse_input(self):
        with open('test', 'r') as f:
            for line in f.readlines():
                self.input.append(list(line.replace("\n","")))
                
    def find_guard(self):
        for row_idx,row in enumerate(self.input):
            try:
                col_idx = row.index("^")
                break
            except:
                pass
            
        self.guard_loc = [row_idx,col_idx]
        return 
      
if __name__ == '__main__':
    p = puzzle()
    p.parse_input()
    p.find_guard()