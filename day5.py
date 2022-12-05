### PART 1 ###
# literally just hardcoding the stacks from my input so I don't have to go
# through the effort of parsing them...
stacks = []

stack1 = ['W', 'B', 'D', 'N', 'C', 'F', 'J']
stacks.append(stack1)

stack2 = ['P', 'Z', 'V', 'Q', 'L', 'S', 'T']
stacks.append(stack2)

stack3 = ['P', 'Z', 'B', 'G', 'J', 'T']
stacks.append(stack3)

stack4 = ['D', 'T', 'L', 'J', 'Z', 'B', 'H', 'C']
stacks.append(stack4)

stack5 = ['G', 'V', 'B', 'J', 'S']
stacks.append(stack5)

stack6 = ['P', 'S', 'Q']
stacks.append(stack6)

stack7 = ['B', 'V', 'D', 'F', 'L', 'M', 'P', 'N']
stacks.append(stack7)

stack8 = ['P', 'S', 'M', 'F', 'B', 'D', 'L', 'R']
stacks.append(stack8)

stack9 = ['V', 'D', 'T', 'R']
stacks.append(stack9)

# print out initial stack configuration
for stack in stacks:
    print(stack)

# grab each line of instructions from the input file
lines = [line[:-1] if line[-1] == '\n' else line for line in open("day5.txt")]

# data class just to keep track of how many crates to move, from what stack, to which stack
class Move:
    def __init__(self, howMany, fromWhere, toWhere):
        self.howMany = howMany
        self.fromWhere = fromWhere
        self.toWhere = toWhere

# list comprehension to take each instruction from the input, 
# and parse out each number to be plugged into our Move class
moves = [Move(int(newMove[1]), int(newMove[3])-1, int(newMove[5])-1) for newMove in [line.split(' ') for line in lines]]
# for each move,
for move in moves:
    print('move ' + str(move.howMany) + ' from ' + str(move.fromWhere+1) + ' to ' + str(move.toWhere+1))
    # do this for however many crates are to be moved:
    for i in range(move.howMany):
        # remember crate to be moved to other stack
        crateMoved = stacks[move.fromWhere][-1]
        # remove crate from stack
        stacks[move.fromWhere].pop()
        # place crate atop the new stack
        stacks[move.toWhere].append(crateMoved)
    for stack in stacks:
        print(stack)

# print out string comprised of the letter corresponding to the crate on top of each stack
print(stacks[0][-1]+stacks[1][-1]+stacks[2][-1]+stacks[3][-1]+stacks[4][-1]+stacks[5][-1]+stacks[6][-1]+stacks[7][-1]+stacks[8][-1])


### PART2 ###
# resetting my hardcoded stacks...
stacks = []

stack1 = ['W', 'B', 'D', 'N', 'C', 'F', 'J']
stacks.append(stack1)

stack2 = ['P', 'Z', 'V', 'Q', 'L', 'S', 'T']
stacks.append(stack2)

stack3 = ['P', 'Z', 'B', 'G', 'J', 'T']
stacks.append(stack3)

stack4 = ['D', 'T', 'L', 'J', 'Z', 'B', 'H', 'C']
stacks.append(stack4)

stack5 = ['G', 'V', 'B', 'J', 'S']
stacks.append(stack5)

stack6 = ['P', 'S', 'Q']
stacks.append(stack6)

stack7 = ['B', 'V', 'D', 'F', 'L', 'M', 'P', 'N']
stacks.append(stack7)

stack8 = ['P', 'S', 'M', 'F', 'B', 'D', 'L', 'R']
stacks.append(stack8)

stack9 = ['V', 'D', 'T', 'R']
stacks.append(stack9)

# list comprehension to take each instruction from the input, 
# and parse out each number to be plugged into our Move class
moves = [Move(int(newMove[1]), int(newMove[3])-1, int(newMove[5])-1) for newMove in [line.split(' ') for line in lines]]
# for each move,
for move in moves:
    print('move ' + str(move.howMany) + ' from ' + str(move.fromWhere+1) + ' to ' + str(move.toWhere+1))
    # temp stack to move multiple crates at a time
    crates = []
    # do this for however many crates are to be moved:
    for i in range(move.howMany):
        # remember crate to be moved to other stack
        crateMoved = stacks[move.fromWhere][-1]
        # remove crate from stack
        stacks[move.fromWhere].pop()
        # place crate atop the temp stack
        crates.append(crateMoved)
    # traverse backward through the temp stack
    for j in reversed(range(len(crates))):
        # place crate atop the new stack
        stacks[move.toWhere].append(crates[j])
    for stack in stacks:
        print(stack)

# print out string comprised of the letter corresponding to the crate on top of each stack
print(stacks[0][-1]+stacks[1][-1]+stacks[2][-1]+stacks[3][-1]+stacks[4][-1]+stacks[5][-1]+stacks[6][-1]+stacks[7][-1]+stacks[8][-1])
