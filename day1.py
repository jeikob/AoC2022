file = open("day1.txt")
inputStr = file.read()

elves = [sum([eval(i) for i in arr.split('\n')]) for arr in inputStr.split('\n\n')]
elves.sort(reverse=True)

print(max(elves))
print(sum(elves[0:3]))
