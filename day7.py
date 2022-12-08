import sys

lines = [line.strip().split(' ') for line in open("day7.txt").readlines()]
sys.setrecursionlimit(1500)

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name, parent, files, directories):
        self.name = name
        self.files = files
        self.directories = directories
        self.parent = parent
    def __repr__(self, level=0):
        printString = "\t"*level + "- " + self.name + " (dir, size =" + str(self.size()) + ")\n"
        for file in self.files:
            printString += "\t"*(level+1) +  "- " + file.name + " (file, size=" + file.size + ")\n"
        for direc in self.directories:
            printString += direc.__repr__(level+1)
        return printString
    def size(self):
        if self.directories == []:
            return sum([int(file.size) for file in self.files])
        else:
            return sum([directory.size() for directory in self.directories]) + sum([int(file.size) for file in self.files])
    def sizeUnder100k(self):
        directoryStr = repr(self)
        strings = [directoryLine.split('(') for directoryLine in directoryStr.split('\n')]
        dirs = [string[-1] for string in strings if string[-1][0:3] == 'dir']
        numbers = [int(direc.split('=')[-1][:-1]) for direc in dirs]
        filteredNumbers = [number for number in numbers if number <= 100000]
        return sum(filteredNumbers)
    def sizeOfDirectoryClosestInSizeTo(self, target):
        directoryStr = repr(self)
        strings = [directoryLine.split('(') for directoryLine in directoryStr.split('\n')]
        dirs = [string[-1] for string in strings if string[-1][0:3] == 'dir']
        numbers = [int(direc.split('=')[-1][:-1]) for direc in dirs]
        closestNum = None
        for number in numbers:
            if closestNum == None:
                closestNum = number
                continue
            if abs(target - number) < abs(target - closestNum) and target - number < 0:
                closestNum = number
        return closestNum

def setupDirectories(direc, i):
    if i == len(lines):
        if direc.parent == None: 
            return direc
        else:
            return setupDirectories(Directory(direc.parent.name, direc.parent.parent, direc.parent.files, \
                                        [directory for directory in direc.parent.directories if directory.name != direc.name] + [direc]), i)
    if lines[i][0] == '$':
        if lines[i][1] == 'cd':
            if lines[i][2] == '..':
                return setupDirectories(Directory(direc.parent.name, direc.parent.parent, direc.parent.files, \
                                            [directory for directory in direc.parent.directories if directory.name != direc.name] + [direc]), \
                                        i+1)
            else:
                return setupDirectories(Directory(lines[i][2], direc, [], []), i+1)
        if lines[i][1] == 'ls':
            return setupDirectories(direc, i+1)
    elif lines[i][0] == 'dir':
        return setupDirectories(Directory(direc.name, direc.parent, direc.files, direc.directories + 
                                    [Directory(lines[i][1], direc, [], [])]), \
                                i+1)
    elif lines[i][0].isnumeric():
        return setupDirectories(Directory(direc.name, direc.parent, \
                                    direc.files + [File(lines[i][1], lines[i][0])], \
                                    direc.directories), \
                                i+1)

fileSystem = setupDirectories(Directory('/', None, [], []), 2)
print(repr(fileSystem), '\n')

#part 1 solution
print('PART 1:')
print(fileSystem.sizeUnder100k(), '\n')

#part 2 solution
print('PART 2')
print('Used Space:')
print(fileSystem.size())
unusedSpace = 70000000 - fileSystem.size()
print('Unused Space:')
print(unusedSpace)
spaceNeededForUpdate = 30000000 - unusedSpace
print('Space Needed for Update:')
print(spaceNeededForUpdate)
closestNum = fileSystem.sizeOfDirectoryClosestInSizeTo(spaceNeededForUpdate)
print('Size of Smallest Directory Needed to Make Space for Update:')
print(closestNum)