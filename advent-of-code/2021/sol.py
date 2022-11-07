def first():
    increases = 0
    with open("first.txt", "r") as f:
        prev = 0
        for line in f.readlines():
            curr = int(line)
            if prev:
                increases += 1 if curr > prev else 0
            prev = curr
                
    return increases

def second():
    increases = 0
    with open("first.txt", "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines)-3):
            if i + 2 < len(lines):
                current = 0
                next = 0
                for j in range(i, i+3):
                    current += int(lines[j])
                for j in range(i+1, i+4):
                    next += int(lines[j])
                increases += 1 if next > current else 0
                
    return increases


if __name__ == '__main__':
    print(first())
    print(second())