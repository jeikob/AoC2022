elves = [sum([eval(i) for i in arr.split('\n')]) for arr in open("day1.txt").read().split('\n\n')]
elves.sort(reverse=True)

print(max(elves)) # part 1 solution
print(sum(elves[0:3])) # part 2 solution