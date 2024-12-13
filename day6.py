class puzzle:

    def __init__(self):
        self.input = []

    def parse_input(self):
        with open('test', 'r') as f:
            for line in f.readlines():
                self.input.append(list(line.replace("\n","")))
                
      
if __name__ == '__main__':
    p = puzzle()
    p.parse_input()

    
    print("Day 6: ")
    print(p.input)