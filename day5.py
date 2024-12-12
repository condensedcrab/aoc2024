class day5:

    def __init__(self):

        self.rules = []
        self.updates = []
        with open('test', 'r') as f:
            for line in f.readlines():
                if "|" in line:
                    self.rules.append(line.strip("\n"))
                elif "," in line:
                    self.updates.append(line.strip("\n"))
                    
        print(self.rules)
        print(self.updates)

if __name__ == '__main__':
    d = day5()

    print(f"\n\nDay 5: ")