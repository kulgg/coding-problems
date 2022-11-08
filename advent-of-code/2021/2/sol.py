
def first():
    depth = 0
    horizontal = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            input = line.split(" ")
            command, steps = input[0], int(input[1])

            if command == "forward":
                horizontal += steps
            elif command == "up":
                depth -= steps
            elif command == "down":
                depth += steps
    
    return depth * horizontal 
        
def second():
    depth = 0
    horizontal = 0
    aim = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            input = line.split(" ")
            command, steps = input[0], int(input[1])

            if command == "forward":
                horizontal += steps
                depth += aim * steps
            elif command == "up":
                aim -= steps
            elif command == "down":
                aim += steps
    
    return depth * horizontal 


if __name__ == '__main__':
    print(first())
    print(second())