with open('input.txt') as f:
    nums = [x.split() for x in f]



def part1(nums):
    shape = {"A":1, "B":2,"C":3, "X":1, "Y":2,"Z":3}
    shape_total = sum([shape[num[1]] for num in nums])
    outcome_total = 0
    for pair in nums:
        if(shape[pair[0]]==shape[pair[1]]):
            outcome_total += 3
        elif(shape[pair[1]]-shape[pair[0]]==1 or (shape[pair[1]]==1 and shape[pair[0]] == 3)):
            outcome_total += 6
    return shape_total+outcome_total

def part2(nums):
    shape = {"A":1, "B":2,"C":3, "X":0, "Y":3,"Z":6}
    outcome_total = sum([shape[num[1]] for num in nums])
    shape_total = 0
    for pair in nums:
        if(pair[1]=="Y"):
            shape_total += shape[pair[0]]
        elif(pair[1]=="Z"):
            if(pair[0]=="C"):
                shape_total += 1
            else:
                shape_total += shape[pair[0]]+1
        else:
            if(pair[0]=="A"):
                shape_total += 3
            else:
                shape_total += shape[pair[0]]-1
    return shape_total+outcome_total

print(part1(nums))
print(part2(nums))