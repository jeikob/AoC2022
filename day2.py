# part 1
strats = [(strat.split(' ')[0], (strat.split(' ')[1])) for strat in open("day2.txt").read().split('\n')]
totalScore = 0
for (them, me) in strats:
    match me:
        case 'X': # +1 rock
            match them:
                case 'A': # +3 rock tie
                    totalScore += 4 # 1+3 rock+tie
                case 'B': # +0 paper loss
                    totalScore += 1 # 1+0 rock+loss
                case 'C': # +6 scissors win
                    totalScore += 7 # 1+6 rock+win
        case 'Y': # +2 paper
            match them:
                case 'A': # +6 rock win
                    totalScore += 8 # 2+6 paper+win
                case 'B': # +3 paper tie
                    totalScore += 5 # 2+3 paper+tie
                case 'C': # +0 scissors loss
                    totalScore += 2 # 2+0 paper+loss
        case 'Z': # +3 scissors
            match them:
                case 'A': # +0 rock loss
                    totalScore += 3 # 3+0 scissors+loss
                case 'B': # +6 paper win
                    totalScore += 9 # 3+6 scissors+win
                case 'C': # +3 scissors tie
                    totalScore += 6 # 3+3 scissors+tie
print(totalScore)

#part 2
strats = [(strat.split(' ')[0], (strat.split(' ')[1])) for strat in open("day2.txt").read().split('\n')]
totalScore = 0
for (them, outcome) in strats:
    match them:
        case 'A': # they choose rock
            match outcome:
                case 'X': #0+3 loss+scissors
                    totalScore += 3
                case 'Y': #3+1 tie+rock
                    totalScore += 4
                case 'Z': #6+2 win+paper
                    totalScore += 8
        case 'B': # they choose paper
            match  outcome:
                case 'X': #0+1 loss+rock
                    totalScore += 1
                case 'Y': #3+2 tie+paper
                    totalScore += 5
                case 'Z': #6+3 win+scissors
                    totalScore += 9
        case 'C': # they choose scissors
            match outcome:
                case 'X': #0+2 loss+paper
                    totalScore += 2
                case 'Y': #3+3 tie+scissors
                    totalScore += 6
                case 'Z': #6+1 win+rock
                    totalScore += 7
print(totalScore)
