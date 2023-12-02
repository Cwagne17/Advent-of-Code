import json

def cmp_list(left_list, right_list):
    if len(left_list) == 0:
        return True
    elif len(right_list) == 0:
        return False

    for i in range(min(len(left_list), len(right_list))):
        res = cmp_element(left_list[i], right_list[i])
        if res:
            return True
        elif isinstance(res, bool):
            return False
    
    if min(len(left_list), len(right_list)) == len(left_list):
        return True
    elif min(len(left_list), len(right_list)) == len(right_list):
        return False

def cmp_element(left_element, right_element):
    if isinstance(left_element, int) and isinstance(right_element, int):
        if left_element == right_element:
            return None
        return min(left_element, right_element) == left_element
    elif isinstance(left_element, list) and isinstance(right_element, list):
        return cmp_list(left_element, right_element)
    else:
        left_element = [left_element] if isinstance(left_element, int) else left_element
        right_element = [right_element] if isinstance(right_element, int) else right_element
        return cmp_list(left_element, right_element) # recursive with two lists now

total = 0
i=1
with open('input.txt') as fin:
    for left, right, _ in list(zip(*[iter([ln.replace('\n', '') for ln in fin.readlines()])]*3)):
        left = json.loads(left)
        right = json.loads(right)
        res = cmp_list(left, right)
        if res:
            total+=i
        i+=1
print(total)
        