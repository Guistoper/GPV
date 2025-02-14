import keyboard

def move_left(board):
    def compress(row):
        return [num for num in row if num != 0] + [0] * (len(row) - len([num for num in row if num != 0]))
    def merge(row):
        for i in range(len(row) - 1):
            if row[i] != 0 and row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
        return row
    new_board = []
    for row in board:
        compressed = compress(row)
        merged = merge(compressed)
        final_row = compress(merged)
        new_board.append(final_row)
    return new_board

start = True
keys = ["left"]
board = [
    [2, 2, 0, 2],
    [4, 0, 4, 4],
    [0, 2, 2, 2],
    [2, 0, 0, 2]
        ]

for row in board:
    print(row)
while start == True:
    for key in keys:
        if keyboard.is_pressed(key):
            print("-" * 50)
            new_board = move_left(board)
            for row in new_board:
                print(row)
            start = False