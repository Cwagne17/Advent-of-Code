calorie_dict = {}

with open('input.txt') as fin:
    calorie_total = 0
    elf_number = 1
    for ln in fin.readlines():
        if ln == "\n":
            calorie_dict[elf_number] = calorie_total
            calorie_total = 0; elf_number += 1
            continue
        calorie_total += int(ln)

max_calories = max(calorie_dict.values())
max_elf_number = max(calorie_dict, key=calorie_dict.get)

## Part 1
print(f"Elf {max_elf_number} has {max_calories} calories.")

## Part 2
calorie_list = list(calorie_dict.values())
calorie_list.sort()

top_3_calories = 0
for cals in calorie_list[-3:]:
    top_3_calories +=cals

print(f"The top 3 elves have a total of {top_3_calories} calories.")