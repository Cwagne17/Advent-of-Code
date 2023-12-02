monkey_dict_list = []

with open('input.txt') as fin:
    monkey_list = []
    monkey_input = []
    
    for ln in [ln.replace('\n', '') for ln in fin.readlines()]:
        if ln == '':
            monkey_list.append(monkey_input)
            monkey_input = []
            continue
        monkey_input.append(ln)
    
    for monkey_data in monkey_list:
        monkey = {
            "number": monkey_data[0].split(" ")[1][0],
            "items": monkey_data[1].split(":")[1].replace(' ', '').split(","),
            "operation": monkey_data[2].split(" ")[-2:],
            "divisble_test": monkey_data[3].split(" ")[-1],
            "true": monkey_data[4].split(" ")[-1],
            "false": monkey_data[5].split(" ")[-1]
        }
        monkey_dict_list.append(monkey)

