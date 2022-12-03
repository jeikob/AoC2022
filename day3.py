import re

### PART 1 ###
# function that takes in letter and produces its priority value
def priority(item):
    lowercase = re.match('[a-z]', item)
    uppercase = re.match('[A-Z]', item)
    if lowercase:
        return ord(item)-96
    elif uppercase:
        return ord(item)-38
# function to find common item between rucksack compartments
def mutualItem(sack1, sack2):
    for item in sack1:
        if item in sack2:
            return item
        else:
            continue
# take in file as input, take string from each line, and present each string as a tuple containing two halves of the string
# ex: ('firstHalf', 'secndHalf') if input string is 'firstHalfsecndHalf'
rucksacks = [(line[slice(0, len(line)//2)], line[slice(len(line)//2, len(line))]) for line in open("day3.txt").read().split('\n')]
# takes the sum of all the priority values of each sack
totalPriority = sum([priority(mutualItem(sack1, sack2)) for (sack1, sack2) in rucksacks])
print(totalPriority)


### PART 2 ###
# read in each elf from the file
elves = open("day3.txt").readlines()
# split out the elves into their respective groups; the [:-1] is just to remove the '\n' from each string 
groups = [(elves[i][:-1], elves[i+1][:-1], elves[i+2][:-1]) for i in range(0, len(elves), 3)]
# function to identify the badge of each group
def groupBadge(elf1, elf2, elf3):
    for badge in elf1:
        if badge in elf2 and badge in elf3:
            return badge
        else:
            continue
# takes the sum of all the priority values for each group's badge
totalGroupsPriority = sum([priority(groupBadge(elf1, elf2, elf3)) for (elf1, elf2, elf3) in groups])
print(totalGroupsPriority)