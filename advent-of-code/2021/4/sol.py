from typing import List

def get_board(lines: List[str]) ->  List[List[int]]:
    res = [[0 for i in range(5)] for i in range(5)]
    row = 0
    col = 0
    number_str = ""
    for line in lines:
        for i in range(len(line)):
            if line[i] == ' ' and number_str:
                res[row][col] = int(number_str)
                if col == 4:
                    col = 0
                    row += 1
                else:
                    col += 1
                number_str = ""
                continue
            if line[i] != ' ':
                number_str += line[i]
            if i == len(line) - 1:
                res[row][col] = int(number_str)
                if col == 4:
                    col = 0
                    row += 1
                else:
                    col += 1
                number_str = ""
    return res

def is_victory(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] != -1:
                break
            if j == 4:
                return True
    for i in range(5):
        for j in range(5):
            if board[j][i] != -1:
                break
            if j == 4:
                return True
    return False


def sum_of_unmarked_numbers(board):
    sum = 0
    for i in range(5):
        for j in range(5):
            sum += board[i][j] if board[i][j] != -1 else 0
    return sum

def first():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        draw_numbers = list(map(int, lines[0].split(",")))
        remaining_lines_size = len(lines) - 1
        boards_num = int(remaining_lines_size / 6)

        boards = []
        for i in range(boards_num):
            start_index = 2 + i*6
            boards.append(get_board(lines[start_index:start_index+6]))
        
        for draw in draw_numbers:
            for i in range(len(boards)):
                for row in range(5):
                    for col in range(5):
                        if boards[i][row][col] == draw:
                            boards[i][row][col] = -1
            
            for board in boards:
                if is_victory(board):
                    return draw * sum_of_unmarked_numbers(board)

def second():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        draw_numbers = list(map(int, lines[0].split(",")))
        remaining_lines_size = len(lines) - 1
        boards_num = int(remaining_lines_size / 6)

        boards = []
        for i in range(boards_num):
            start_index = 2 + i*6
            boards.append(get_board(lines[start_index:start_index+6]))
        
        for draw in draw_numbers:
            for i in range(len(boards)):
                for row in range(5):
                    for col in range(5):
                        if boards[i][row][col] == draw:
                            boards[i][row][col] = -1
            
            to_delete = []
            for i in range(len(boards)):
                if is_victory(boards[i]):
                    if len(to_delete) == len(boards) - 1:
                        return draw * sum_of_unmarked_numbers(boards[i])
                    to_delete.append(i)
            boards = [v for i, v in enumerate(boards) if i not in to_delete]


if __name__ == '__main__':
    print(first())
    print(second())
