lines = [line[:-1] if line[-1] == '\n' else line for line in open("day4.txt").readlines()]
elves = [(line.split(',')[0], line.split(',')[1]) for line in lines]
ranges = [((int(elf1.split('-')[0]), int(elf1.split('-')[1])), (int(elf2.split('-')[0]), int(elf2.split('-')[1]))) for (elf1, elf2) in elves]

# part 1
containedRanges = ['in' for ((elf1Begin, elf1End), (elf2Begin, elf2End)) in ranges if (elf1Begin <= elf2Begin and elf1End >= elf2End) or (elf2Begin <= elf1Begin and elf2End >= elf1End)]
print(len(containedRanges))

# part 2
overlappingRanges = ['overlapped' for ((elf1Begin, elf1End), (elf2Begin, elf2End)) in ranges if (elf1Begin >= elf2Begin and elf1Begin <= elf2End) or (elf2Begin >= elf1Begin and elf2Begin <= elf1End)]
print(len(overlappingRanges))