class day5:

    def __init__(self):

        self.rules = {}
        self.updates = []
        with open('test', 'r') as f:
            for line in f.readlines():
                if "|" in line:
                    temp_str = line.strip("\n").split('|')
                    self.rules[temp_str[0]] = temp_str[1]
                elif "," in line:
                    self.updates.append(line.strip("\n"))
                    
        print(self.rules)
        print(self.updates)
        
    def verify_updates(self):
        
        for update in self.updates:
            splits = update.split(",")
            
            for s in splits:
                r = self.rules.get('s')
                if r is None:
                    continue
                else:
                    if update.find(r) < update.find(s):
                        continue
                    else:
                        print(f"Rule satisfied: {s} is before {r} in update: {update}")


if __name__ == '__main__':
    d = day5()

    print(f"\n\nDay 5: ")