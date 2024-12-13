class day5:

    def __init__(self):

        self.rules = []
        self.updates = []
        with open('test', 'r') as f:
            for line in f.readlines():
                if "|" in line:
                    temp_str = line.strip("\n").split('|')
                    self.rules.append(temp_str)
                elif "," in line:
                    self.updates.append(line.strip("\n"))
                    
        print(self.rules)
        print(self.updates)
        self.correct = []
        self.incorrect = []
        self.amended = []
        self.correct_sum = 0
        self.amended_sum = 0
        
    def verify_updates(self):
        """
        Loop through updates and check against the ruleset provided. Use a flag to track validity and only toggle flag to false if a rule is found to be broken.
        """
        for update in self.updates:
            print(f"\nInput data is: {update}")
            update_validity = True
            splits = update.split(",")

            broken_rules = []
            for s in splits:
                for rule in self.rules:
                    if rule[0] == s:
                        r = rule[1]

                        if update.find(r) == -1:
                            # print(f"Rule was {s}|{r}, but {r} was not found.")
                            continue
                        elif update.find(r) < update.find(s):
                            print(f"Rule broken: {s}|{r}.")
                            update_validity = False
                            broken_rules.append(rule)
                        elif update.find(r) > update.find(s):
                            # print(f"Rule satisfied: {s} is before {r}.")
                            continue
            
            if update_validity:
                self.correct.append(update)
            else:
                self.incorrect.append([update,broken_rules])

    def sum_middle_updates(self):
        for l in self.correct:
            split_nums = l.split(",")
            idx = int((len(split_nums)-1)/2)
            # print(f"Correct update is: {l}. Middle number is: {int(split_nums[idx])}.")
            self.correct_sum += int(split_nums[idx])
            
    def rearrange_incorrect(self):
        
        for update in self.incorrect:
            # print(f"\nIncorrect update is: {update[0]}")
            # print(f"Broken rules are: {update[1]}")

            splits = update[0].split(",")
            rearr = splits
            broken_rules = update[1]
            
            for idx,val in enumerate(rearr):
                
                indices = []
                for rule in broken_rules:
                    if val == rule[0] and rule[1] in rearr:
                        indices.append(rearr.index(rule[1]))
                
                if len(indices) > 0:
                    # print(rearr)
                    rearr.pop(idx)
                    # print(rearr)
                    rearr.insert(min(indices),val)
                    # print(rearr)

            # print(f"Original update was: \n{splits}.") #\nRules broken were: {broken_rules}")
            # print(f"Update has been modified to: \n{rearr}")
            
            self.amended.append(rearr)

    def sum_middle_amended_updates(self):
        for l in self.amended:
            idx = int((len(l)-1)/2)
            print(f"Amended update is: {l}. Middle number is: {int(l[idx])}.")
            self.amended_sum += int(l[idx])
if __name__ == '__main__':
    d = day5()

    print(f"\n\nDay 5: ")
    
    d.verify_updates()
    d.sum_middle_updates()
    print(f"Sum of middle item from correct updates is: {d.correct_sum}")
    
    # part 2
    d.rearrange_incorrect()
    d.sum_middle_amended_updates()
    print(f"Sum of middle item from re-arranged incorrect updates is: {d.amended_sum}")
    