def part1(input):
    fresh_ids = input['fresh']
    available_ids = input['available']
    num_fresh = 0

    for id in available_ids:
        for fresh in fresh_ids:
            if fresh[0] <= id <= fresh[1]:
                num_fresh += 1
                break

    print(num_fresh)
            

def part2(input):

    def check_range(id_range:tuple, check_existing=False):
        range_overlap = False
        for i in range(0, len(all_ranges)):
            if all_ranges[i][0] <= id_range[0] <= all_ranges[i][1]:
                if all_ranges[i][1] < id_range[1]:
                    all_ranges[i] = (all_ranges[i][0], id_range[1])
                    range_overlap = True
            if id_range[0] < all_ranges[i][0] < id_range[1]:
                if all_ranges[i][1] < id_range[1]:
                    all_ranges[i] = (id_range[0], id_range[1])
                    range_overlap = True
                else:
                    all_ranges[i] = (id_range[0], all_ranges[i][1])
                    range_overlap = True
            if range_overlap:
                break
        if not range_overlap and not check_existing:
            all_ranges.append(id_range)
        elif not check_existing:
            for id_range in all_ranges:
                check_range(id_range=id_range, check_existing=True)
            

    fresh_ids = input['fresh']
    all_ranges = []
    for id_range in fresh_ids:
        check_range(id_range=id_range)
    all_ranges = set(all_ranges)
    num_ids = 0
    for id_range in all_ranges:
        num_ids += id_range[1] - id_range[0] + 1
    
    print(num_ids)

def parse_input():
    with open("day5/input.txt", 'r') as f:
        input = f.read()

    data = {}
    
    # Get fresh IDs
    fresh_ids = input.split("\n\n")[0].split("\n")
    data['fresh'] = []
    for id_row in fresh_ids:
        min_id, max_id = int(id_row.split('-')[0]), int(id_row.split('-')[1])
        data['fresh'].append((min_id, max_id))
    
    # Get available IDs
    avaiable_ids = input.split("\n\n")[1].split("\n")
    data['available'] = [int(x) for x in avaiable_ids]
    return data
    

if __name__ == '__main__':
    input = parse_input()
    part1(input)
    part2(input)