def first():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        map_length = 1000
        ground_map = [[0 for i in range(map_length)] for j in range(map_length)]

        for line in lines:
            segments = line.split(" ")
            start_coordinates = segments[0].split(",")
            end_coordinates = segments[2].split(",")
            x1, y1 = int(start_coordinates[0]), int(start_coordinates[1])
            x2, y2 = int(end_coordinates[0]), int(end_coordinates[1])

            if x1 == x2:
                smaller = min(y1, y2)
                larger = max(y1,y2)
                for i in range(smaller, larger+1):
                    ground_map[x1][i] += 1
            if y1 == y2:
                smaller = min(x1, x2)
                larger = max(x1,x2)
                for i in range(smaller, larger+1):
                    ground_map[i][y1] += 1
        
        bad_points = 0
        for i in range(map_length):
            for j in range(map_length):
                if ground_map[i][j] >= 2:
                    bad_points += 1
        return bad_points

def second():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        map_length = 1000
        ground_map = [[0 for i in range(map_length)] for j in range(map_length)]

        for line in lines:
            segments = line.split(" ")
            start_coordinates = segments[0].split(",")
            end_coordinates = segments[2].split(",")
            x1, y1 = int(start_coordinates[0]), int(start_coordinates[1])
            x2, y2 = int(end_coordinates[0]), int(end_coordinates[1])

            if x1 == x2:
                smaller = min(y1, y2)
                larger = max(y1,y2)
                for i in range(smaller, larger+1):
                    ground_map[x1][i] += 1
            elif y1 == y2:
                smaller = min(x1, x2)
                larger = max(x1,x2)
                for i in range(smaller, larger+1):
                    ground_map[i][y1] += 1
            else:
                x_direction = 1 if x2 > x1 else -1
                y_direction = 1 if y2 > y1 else -1
                while x1 != x2 + x_direction:
                    ground_map[x1][y1] += 1
                    x1 += x_direction
                    y1 += y_direction
        
        bad_points = 0
        for i in range(map_length):
            for j in range(map_length):
                if ground_map[i][j] >= 2:
                    bad_points += 1
        return bad_points

if __name__ == '__main__':
    print(first())    
    print(second())    