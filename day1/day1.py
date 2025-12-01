

def part1():
    # Parse input
    with open("day1/input.txt", 'r') as file:
        turns = file.readlines()
    
    # Starts at 50
    pos = 50
    num_zero = 0

    # Iterate over each turn
    for turn in turns:
        turn = turn.strip()
        dir = turn[0]
        value = int(turn[1:])

        if dir == "R":
            pos = pos + (value % 100)
            if pos > 99:
                pos -= 100
        else:
            pos = pos - (value % 100)
            if pos < 0:
                pos += 100
                
        if pos == 0:
            num_zero += 1

    print(num_zero)




def part2():
    pass


if __name__ == '__main__':
    part1()
    part2()