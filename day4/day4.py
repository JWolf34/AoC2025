def part1(input: list):

    def is_valid_pos(x,y):
        if 0 <= x < len(input) and 0 <=y < len(input[x]):
            return True
        return False

    def get_num_adjacent_rolls(row, col):

        adjacent = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if not (x == y == 0) and is_valid_pos(row+x, col+y):
                    adjacent.append(input[row+x][col+y])
        return adjacent.count('@')

    bangs = 0
    # Iterate over grid
    for row in range(0, len(input)): # Rows
        for col in range(0, len(input[row])): # Cols
            if input[row][col] == '@':
                num_rolls = get_num_adjacent_rolls(row=row, col=col)
                if num_rolls < 4:
                    bangs +=1

    print(bangs)




def part2(input: list):
    def is_valid_pos(x,y):
        if 0 <= x < len(input) and 0 <=y < len(input[x]):
            return True
        return False

    def get_num_adjacent_rolls(row, col):

        adjacent = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if not (x == y == 0) and is_valid_pos(row+x, col+y):
                    adjacent.append(input[row+x][col+y])
        return adjacent.count('@')
    
    def remove_rolls(indicies: list):
        for (x,y) in indicies:
            input[x][y] = 'X'
    
    def get_num_bangs():

        bangs = 0
        indices = []
        # Iterate over grid
        for row in range(0, len(input)): # Rows
            for col in range(0, len(input[row])): # Cols
                if input[row][col] == '@':
                    num_rolls = get_num_adjacent_rolls(row=row, col=col)
                    if num_rolls < 4:
                        bangs +=1
                        indices.append((row, col))
        remove_rolls(indicies=indices)
        return bangs

    total_bangs = 0
    while True:
        new_bangs = get_num_bangs()
        if new_bangs == 0:
            break
        else:
            total_bangs += new_bangs

    print(total_bangs)
                

def parse_input():
    with open("day4/input.txt") as file:
        data = file.read().split("\n")
        grid  = []
        for i in range(0, len(data)):
            grid.append([])
            for j in range(0, len(data[i])):
                grid[i].append(data[i][j])

        return grid

if __name__ == '__main__':
    input = parse_input()
    part1(input=input)
    part2(input=input)
