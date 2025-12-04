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
    from collections import defaultdict

    jolts = []
    for bank in input:

        # We need 12 digits, so get the highest number in the first 4 digits
        # Then we can find the biggest number of the remaining digits

        battery_jolts = []
        battery_bank = [x for x in bank.strip()]
        batteries = list(battery_bank)

        first_digit = max(battery_bank[:4])
        first_digit_index = battery_bank.index(first_digit)
        batteries = batteries[first_digit_index+1:]

        index_map = defaultdict(list)
        for index, x in enumerate(batteries):
            index_map[x].append(index)

        for i in range(0, 11):
            jolt_value = max(index_map)
            jolt_index = max(index_map[jolt_value])

            if not index_map[jolt_value]:
                index_map.pop(jolt_value)

            battery_jolts.append({"value": jolt_value,
                                 "index":jolt_index})
            
        battery_jolts = sorted(battery_jolts, key=lambda battery: battery['index'])
        jolts.append(int(first_digit + ''.join(x['value'] for x in battery_jolts)))

        #combos = [int(''.join(x)) for x in combinations(batteries, 11)]
        #jolts.append(int(str(first_digit) + str(max(combos))))

    print(sum(jolts))
        

def parse_input():
    with open("day3/input.txt", 'r') as file:
        data = file.readlines()
    return data

if __name__ == '__main__':
    input = parse_input()
    part1(input=input)
    part2(input=input)