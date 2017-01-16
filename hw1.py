"""The purpose of the program is to analyze and graph score data from a user defined file. Uses list and dictionaries"""
print('Welcome to the Quiz Score Frequency Analyzer')
# file input
fileName = input("Enter file path: ")
print('Reading file \'', fileName, '\' input:')
# read file and strip blank lines
with open(fileName) as f:
    lineList = [line.strip() for line in f if line.strip()]
# print out all of the score key-values
for tup in lineList:
    print(tup)
# initialize dictionary D and populate it with key-value data
D = {}
for line in lineList:
    tmp = line.split()
# if key already exists, add the values together to prevent duplicates
    if D.__contains__(tmp[0]):
        D[tmp[0]] = int(tmp[1]) + int(D[tmp[0]])
# else create new key
    else:
        D[tmp[0]] = int(tmp[1])
print('\nThe smallest score value is', min(D), '\nThe largest score value is', max(D))
print('The largest frequency is', D[max(D, key=D.get)], '\n\n--Input Data--\nScore: Frequency Bar Chart', '\n')
maxScore = int(max(D))
minScore = int(min(D))
# first graph, print within the range of the min and max scores
for i in range(minScore, maxScore + 1):
    if D.__contains__(str(i)):
        # formatting if number is greater than 10
        if D[str(i)] >= 10:
            print(i, ':', D[str(i)], '  ', end='')
        elif D[str(i)] < 10:
            print(i, ': ', D[str(i)], '  ', end='')
        for a in range(D[str(i)]):
            print('*', end='')
        print('')
    else:
        print(i, ': ', 0)
# second graph, print from max frequency to 0
print('\nFrequency: Score Bar Chart\n')
count = D[max(D, key=D.get)]
while count > 0:
    # formatting if number is greater than 10
    if count >= 10:
        print('   ^  ', count, ':', end='')
    elif count < 10:
        print('   ^   ', count, ':', end='')
    for i in range(minScore, maxScore + 1):
        # print a star if the score frequency is >= the current printed frequency
        if D.__contains__(str(i)):
            if D[str(i)] >= count:
                print('  *', end='')
            else:
                print('   ', end='')
        else:
            print('   ', end='')
    print('')
    count -= 1
print('__________:', end='')
for i in range(minScore, maxScore + 1):
    print('__^', end='')
print('\n     Score:', end='')
for z in range(minScore, maxScore + 1):
    print('', z, end='')
