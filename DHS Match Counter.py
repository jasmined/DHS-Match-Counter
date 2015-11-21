##########################################################################
#INPUT
def main():
    attendees = input('Enter the name of the file with attendees names: ')
    suspects = input('Enter the name of the file with suspect names: ')

    aFile = open(attendees, 'r')
    sFile = open(suspects, 'r')
    outputFile = open('matches.csv', 'w')

    attList = []
    susList = []

    #append the attendee names and suspect names to two lists
    for att in aFile:
        attList.append(att.strip())
    for sus in sFile:
        susList.append(sus.strip())

    #calls the matchChar function to count the matches and returns
    #a percentage. All matches over 70% will be appended to susMatch
    susMatch = []
    for susName in susList:
        for attName in attList:
            percent = matchChar(susName, attName)
            if percent >= 70:
                susMatch.append([susName, attName, percent])
    
    #prints all matches over 90% and keeps a count of them
    match = 0
    for sus in susList:
        for att in attList:
            percent = matchChar(sus, att)
            if percent == 100:
                print('###################################')
                print('PERFECT MATCH')
                print('Threat: {}'.format(sus))   
                print('Attendees: {}'.format(att))
                print('###################################')
                print()
                match += 1
            elif percent >= 90:
                print('###################################')
                print('Match > 90%')
                print('Threat: {}'.format(sus))
                print('Attendees: {}'.format(att))
                print('###################################')
                print()
                match +=1
    print('[90, 100] match count: {}'.format(match))

    outputFile.write('Suspect Name, Matches\n')
    for name in susList:
        outputFile.write(name +'\n')
        seventyList = []
        eightyList = []
        ninetyList = []
        oneHundredList = []
        for idx in range(len(susMatch)):
            if name == susMatch[idx][0]:
                if susMatch[idx][2] == 100:
                    oneHundredList.append(susMatch[idx][1])
                elif susMatch[idx][2] >= 90:
                    ninetyList.append(susMatch[idx][1])
                elif susMatch[idx][2] >= 80:
                    eightyList.append(susMatch[idx][1])
                elif susMatch[idx][2] >= 70:
                    seventyList.append(susMatch[idx][1])

    #writes matches to file
        outputFile.write('100% matches: ')
        outputFile.write(str(len(oneHundredList)) + str(','))
        for each in oneHundredList:
            outputFile.write(each + str(','))
        outputFile.write(str('\n'))
        outputFile.write('90% matches: ')
        outputFile.write(str(len(ninetyList))+ str(','))
        for each in ninetyList:
            outputFile.write(each + str(','))
        outputFile.write(str('\n'))
        outputFile.write('80% matches: ')
        outputFile.write(str(len(eightyList))+ str(','))
        for each in eightyList:
            outputFile.write(each + str(','))
        outputFile.write(str('\n'))
        outputFile.write('70% matches: ')
        outputFile.write(str(len(seventyList))+ str(','))
        for each in seventyList:
            outputFile.write(each + str(','))
        outputFile.write(str('\n'))
            
    aFile.close()
    sFile.close()
    outputFile.close()

#pre : takes an attendee and suspect name
#post: returns the percentage match count
def matchChar(sName, aName):   
    #variables for the matching process
    vowels = 'AEIOU'
    con = 'BCDFGHJKLMNPQRSTVWXYZ'
    sym = '@'
    sym2 = '$'

    #length calculated for the percentage calculation
    #Subtracts one to not count the space as part of the length
    length = (max(len(sName), len(aName)) - 1)
    countF = 0
    countL = 0
    
    #names are split for the matches to be counted separately for
    #first and last names
    susSplit = sName.split()
    attSplit = aName.split()
    
    #iterate over each letter in the first names and count the matches
    for i in range(min(len(susSplit[0]), len(attSplit[0]))):
        if susSplit[0][i] == attSplit[0][i]:
            countF += 1
        elif susSplit[0][i] == sym and ((attSplit[0][i] in vowels)):
            countF += 0.75
        elif susSplit[0][i] == sym2 and ((attSplit[0][i] in con)):
            countF += 0.5
        else:
            countF += 0

    #iterate over each letter in the last names and count the matches
    for i in range(min(len(susSplit[-1]), len(attSplit[-1]))):
        if susSplit[1][i] == attSplit[1][i]:
            countL += 1
        elif susSplit[1][i] == sym and ((attSplit[1][i] in vowels)):
            countL += 0.75
        elif susSplit[1][i] == sym2 and ((attSplit[1][i] in con)):
            countL += 0.5
        else:
            countL += 0

    count = countF + countL
    percent = (count / length) * 100

    return percent

main()
