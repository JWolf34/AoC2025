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
    from collections import defaultdict

    jolts = []
    for bank in input:
        battery_jolts = []
        battery_bank = [int(x) for x in bank.strip()]
        batteries = list(battery_bank)
        index_map = defaultdict(battery_bank)
        for i in range(0, 12):
            
            jolt_value = max(index_map)
            jolt_index = max(index_map[jolt_value])
            index_map[jolt_value].remove(jolt_index)

            if not index_map[jolt_value]:
                index_map.pop(jolt_value)

            jolt = {'value': jolt_value,
                    'index': jolt_index}
            battery_jolts.append(jolt)
        
        battery_jolts = sorted(battery_jolts, key= lambda jolt: jolt['index'])
        jolts.append(int(''.join([str(jolt['value']) for jolt in battery_jolts])))

    print(sum(jolts))
        

def parse_input():
    with open("day3/test_input.txt", 'r') as file:
        data = file.readlines()
    return data

if __name__ == '__main__':
    input = parse_input()
    part1(input=input)
    part2(input=input)