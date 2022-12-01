

# get input dat from file
def get_input():
    input = [x for x in open('input.txt').read().splitlines()]
    return input #[int(line) for line in f.readlines()]

# get list of Elf, each int represet item calories, each elf separetes their won inventory with ''
def get_elves_inventory(input):
    elves = []
    elf = []
    for line in input:
        if line == '':
            elves.append(elf)
            elf = []
        else:
            elf.append(line)
    elves.append(elf)
    return elves

# get sum of all items calories in one elf inventory
def get_elf_inventory_calories(elf):
    calories = 0
    for item in elf:
        calories += int(item.split(' ')[-1])
    return calories

# wich elf has the most calories in his inventory
def get_elf_with_most_calories(elves):
    max_calories = 0
    max_calories_elf = 0
    for elf in elves:
        calories = get_elf_inventory_calories(elf)
        if calories > max_calories:
            max_calories = calories
            max_calories_elf = elves.index(elf)
    return max_calories_elf 

# get 3 elf with most calories
# def get_3_elf_with_most_calories(elves):
#     elf1 = get_elf_with_most_calories(elves)
#     elves.pop(elf1)
#     elf2 = get_elf_with_most_calories(elves)
#     elves.pop(elf2)
#     elf3 = get_elf_with_most_calories(elves)
#     elves.pop(elf3)
#     return [elf1, elf2, elf3]

# order elves by calories
def order_elves_by_calories(elves):
    elves_calories = []
    for elf in elves:
        elves_calories.append(get_elf_inventory_calories(elf))
    elves_calories.sort(reverse=True)
    return elves_calories

def main():
    input = get_input()
    elves = get_elves_inventory(input)
    index_most_calories_elf = get_elf_with_most_calories(elves)
    most_caliries_elf = get_elf_inventory_calories(elves[index_most_calories_elf])
    print(f'Elf number {index_most_calories_elf+1} is carrying the most Calories: {most_caliries_elf}')

    elves_calories = order_elves_by_calories(elves)
    print(f'Elf number {elves.index(elves[elves_calories.index(elves_calories[0])])+1} is carrying the most Calories: {elves_calories[0]}')
    print(f'Elf number {elves.index(elves[elves_calories.index(elves_calories[1])])+1} is carrying the most Calories: {elves_calories[1]}')
    print(f'Elf number {elves.index(elves[elves_calories.index(elves_calories[2])])+1} is carrying the most Calories: {elves_calories[2]}')
    sum_of_3_elves = elves_calories[0] + elves_calories[1] + elves_calories[2]
    print(f'The sum of the 3 elves with the most Calories is: {sum_of_3_elves}')
    
    # three_elves = get_3_elf_with_most_calories(elves)
    # print(f'Elf number {three_elves[0]+1}, {three_elves[1]+1} and {three_elves[2]+1} are carrying the most Calories')
    # total_calories = get_elf_inventory_calories(elves[three_elves[0]])# + get_elf_inventory_calories(elves[three_elves[1]]) + get_elf_inventory_calories(elves[three_elves[2]])
    # print(f'Their total Calories is: {total_calories}')
    


main()

