import sys
import string
import pandas as pd

def openDictionary():
    file = open("dict.txt", "r")
    lst = []
    for line in file:
        lst.append(line.strip().lower())
    return lst

def openBonus():
    mp = [[a, False] for a in string.ascii_lowercase[:26]]
    return mp

def copyToClipboard(word):
    df = pd.DataFrame([word])
    df.to_clipboard(index = False, header = False)

words = openDictionary()
bonus = openBonus()

waiting = False
works = []
nextCandidate = -1


for line in sys.stdin:
    key = line.strip()
    print("Your Input: " + key)

    if 'q' == key:
        break
    elif waiting == True:
        if key == "next":
            nextCandidate += 1

            print("Word: " + works[nextCandidate][0])

        else:
            copyToClipboard(works[nextCandidate][0])

            for i in range(len(bonus)):
                if bonus[i][0] in word:
                    bonus[i][1] = True
            # print("Current Bonus: " + str(bonus))
            
            waiting = False
    else:
        works = []
        for word in words:
            if key in word:
                bonusCnt = 0
                for i in range(len(bonus)):
                    if bonus[i][1]==False and bonus[i][0] in word:
                        bonusCnt+=1(
                works.append([word, bonusCnt])
        works = sorted(works, reverse = True, key = lambda x : x[1])
        
        nextCandidate = 0
        print("Word: " + works[nextCandidate][0])
        waiting = True
        

    print("waiting for your input...")