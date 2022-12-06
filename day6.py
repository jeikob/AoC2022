inputStr = open("day6.txt").read()

def findMarker(signal, markerType):
    if markerType == 'packet': markerLength = 4
    if markerType == 'message': markerLength = 14
    for i in range(len(signal)):
        possibleMarker = signal[i:i+markerLength]
        notMarker = False
        for letter in possibleMarker:
            if possibleMarker.count(letter) > 1:
                notMarker = True
                break
            else:
                continue
        if notMarker is False:
            return i+markerLength
        else:
            notMarker = False
            continue

print(findMarker(inputStr, 'packet'))
print(findMarker(inputStr, 'message'))