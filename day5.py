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
        self.correct = []
        
    def verify_updates(self):
        
        for update in self.updates:
            update_validity = True
            splits = update.split(",")
            
            for s in splits:
                r = self.rules.get(s)
                if r is None:
                    continue
                else:
                    if update.find(r) == -1:
                        print(f"Dictionary key was {s}, and rule was {s}|{r}, but {r} was not found.")
                        continue
                    elif update.find(r) < update.find(s):
                        print(f"Dictionary key was {s}, and rule was {s}|{r}, but {r} was before {s}. \nInput was: {update}\n")
                        update_validity = False
                        continue
                    else:
                        print(f"Rule satisfied: {s} is before {r} in update: {update}")
            
            if update_validity:
                self.correct.append(update)


if __name__ == '__main__':
    d = day5()

    print(f"\n\nDay 5: ")
    
    d.verify_updates()
    print(d.correct)
