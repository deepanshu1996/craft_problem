# First we count the frequency of each character in the input string
# Then we count the removals by iterating through all the unique characters 
# and removing previously used frequencies
# Time complexity O(len(musicalString)) Space Complexity O(1)
def minDeletions(musicalString):
    charCounts = {}
    
    for ch in musicalString:
        charCounts[ch] = charCounts.get(ch,0) + 1
        
    seenFrequencies = set()
    removals = 0
    for ch, count in charCounts.items():
        while count > 0 and count in seenFrequencies:
            count -= 1
            removals += 1
        seenFrequencies.add(count)
        
    return removals

# after sorting the input string
# we check for unique frequency of each character which appears in the order
# if the character with the current frequency is already present in seenFrequencies 
# we need to keep on increasing the removals till we get a new frequency
# N = len(musicalString)
# Time complexity O(N(logN)) Space Complexity O(1)
def minDeletionsApproach2(musicalString):
    seenFrequencies = set()
    removals = 0

    musicalString = sorted(musicalString)
    prevCh = musicalString[0]
    currLen = 1
    
    def checkAndAddFrequency():
        nonlocal currLen
        nonlocal removals
        while currLen in seenFrequencies:
            removals += 1
            currLen -= 1
    
    for i in range(1,len(musicalString)):
        ch = musicalString[i]
        if ch == prevCh:
            currLen += 1
        else:
            checkAndAddFrequency()
            if currLen > 0:
                seenFrequencies.add(currLen)
            currLen = 1
            prevCh = ch
    checkAndAddFrequency()

    return removals


if __name__ == "__main__":
    musical_string = input()
    print(minDeletions(musical_string))
