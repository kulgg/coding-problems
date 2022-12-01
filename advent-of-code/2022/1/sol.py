
def first():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        
        max_calories = 0
        current_elve = 0

        for line in lines:
            if line == "\n":
                max_calories = max(max_calories, current_elve)
                current_elve = 0
            else:
                current_elve += int(line[:-1])
        return max_calories

def second():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        
        elve_cals = []
        current_elve = 0

        for line in lines:
            if line == "\n":
                elve_cals.append(current_elve)
                current_elve = 0
            else:
                current_elve += int(line[:-1])

        return sum(sorted(elve_cals)[-3:])
    

if __name__ == "__main__":
    print(first())
    print(second())