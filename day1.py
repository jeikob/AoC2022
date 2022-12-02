elves = [sum([eval(i) for i in arr.split('\n')]) for arr in open("day1.txt").read().split('\n\n')]
elves.sort(reverse=True)

print(max(elves))
print(sum(elves[0:3]))