def first():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        bits = len(lines[0])
        majority = [0 for i in range(bits)]

        for line in lines:
            for i in range(bits):
                majority[i] += 1 if line[i] == '1' else -1
        
        gamma = 0
        epsilon = 0

        for i in range(bits-1, -1, -1):
            gamma += (1 << bits-1-i) if majority[i] >= 0 else 0
            epsilon += (1 << bits-1-i) if majority[i] < 0 else 0
        
        return gamma * epsilon

def second():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        oxygen = [line for line in lines]
        scrubber = [line for line in lines]
        bits = len(lines[0])

        for bit in range(bits):
            majority = 0
            for line in oxygen:
                majority += 1 if line[bit] == '1' else -1
            favored_bit = '1' if majority >= 0 else '0'
            for line in lines:
                if line in oxygen and favored_bit != line[bit]:
                    oxygen.remove(line)
            if len(oxygen) == 1:
                break

        for bit in range(bits):
            majority = 0
            for line in scrubber:
                majority += 1 if line[bit] == '1' else -1
            favored_bit = '0' if majority >= 0 else '1'
            for line in lines:
                if line in scrubber and favored_bit != line[bit]:
                    scrubber.remove(line)
            if len(scrubber) == 1:
                break

        return int(oxygen[0], 2) * int(scrubber[0], 2)

if __name__ == '__main__':
    print(first())
    print(second())