def part1(input: list):
    jolts = []
    for bank in input:
        battery_bank = [int(x) for x in bank.strip()]
        batteries = list(battery_bank)

        # Get first max jolt
        first_max_jolt = max(batteries)
        first_jolt_index = battery_bank.index(first_max_jolt)
        second_max_jolt = 0

        # Get second max jolt

        # If first max_jolt at the end of the list, find max in list before this index
        if first_jolt_index == len(battery_bank) - 1:
            second_max_jolt = max(batteries[:first_jolt_index])
            jolt = int(str(second_max_jolt) + str(first_max_jolt))
        # Else, find max in list after this index
        else:
            second_max_jolt = max(batteries[first_jolt_index+1:])
            jolt = int(str(first_max_jolt) + str(second_max_jolt))

        jolts.append(jolt)
    
    print(sum(jolts))



def part2(input: list):
    from itertools import combinations

    jolts = []
    for bank in input:
        battery_jolts = []
        battery_bank = [x for x in bank.strip()]
        combos = [int(''.join(x)) for x in combinations(battery_bank, 12)]
        jolts.append(max(combos))

    print(sum(jolts))
        

def parse_input():
    with open("day3/test_input.txt", 'r') as file:
        data = file.readlines()
    return data

if __name__ == '__main__':
    input = parse_input()
    part1(input=input)
    part2(input=input)