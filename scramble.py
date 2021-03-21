# Program Purpose
# Makes the words in a sentence scambled

# Name: Bartek Kowalski
# Date: 2021-03-21

from random import randint

# Welcome
print("Welcome to my program! It scrambles a sentence that was inputted.")


def main():
    sentence = input("Enter a sentence without the period at the end: ")
    listsentence = sentenceSplit(sentence)
    newSentence = sentenceRandom(listsentence)
    print(''.join(newSentence))


def sentenceSplit(sentence):
    x = sentence.split()
    return x


def sentenceRandom(listsentence):
    global let2
    newlist = []
    x = 0
    for i in listsentence:
        if len(listsentence[x]) > 3:
            let1 = randint(1, len(listsentence[x]) - 2)
            redo = True
            while redo:
                let2 = randint(1, len(listsentence[x]) - 2)
                if let2 != let1:
                    redo = False
            if i[let1] == i[let2] and len(i) != 4:
                let1, let2 = check(let1, let2, i)
            new = replace(let1, let2, i)
            newlist.append(new + " ")
        else:
            newlist.append(listsentence[x] + " ")
        x += 1
    return newlist


def check(let1, let2, i):
    redo = True
    while redo:
        if i[let1] != i[let2]:
            return let1, let2
        else:
            let2 = randint(1, len(i) - 2)


def replace(let1, let2, i):
    y = 0
    num1 = i[let1]
    num2 = i[let2]
    listword = list(i)
    for x in listword:
        if y == let1:
            listword.remove(listword[y])
            listword.insert(y, num2)
        if y == let2:
            listword.remove(listword[y])
            listword.insert(y, num1)
        y += 1
    a = ''.join(listword)
    return a


main()

# end
print("Thank you for using my program!")

