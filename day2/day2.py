import regex as re

def part1(input: list):

    def is_repdigit(digit: int):
        digit = str(digit)

        # If digit is not even, it cannot be a repdigit
        if len(digit) % 2 != 0:
            return False

        # When split, does the digit repeat?
        firstpart, secondpart = digit[:len(digit)//2], digit[len(digit)//2:]
        if firstpart == secondpart:
            return True


    invalid_ids = []
    for id in input:
        id = id.split('-')
        first_id = int(id[0])
        last_id = int(id[1])

        for i in range(first_id, last_id):
            if is_repdigit(i):
                invalid_ids.append(i)
    
    print(sum(invalid_ids))






def part2(input: list):
    def contains_repdigit(digit: int):
        digit = str(digit)
        
        if digit == '111':
            pass
        
        for i in range(0, len(digit)//2):
            first_substr = digit[:i+1]
            for j in range(i+1, len(digit)):
                second_substr = digit[i+1:j+1]
                if first_substr == second_substr:
                    return True
        
        return False
        
        


    invalid_ids = []
    for id in input:
        id = id.split('-')
        first_id = int(id[0])
        last_id = int(id[1])

        for i in range(first_id, last_id+1):
            if contains_repdigit(i):
                invalid_ids.append(i)
    
    print(invalid_ids)
    print(sum(invalid_ids))


def parse_input():
    # Parse input
    with open("day2/test_input.txt", 'r') as file:
        input = file.read()
        input = input.split(',')
    
    return input
    

if __name__ == "__main__":
    input =  parse_input()
    part1(input=input)
    part2(input=input)