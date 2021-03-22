# Program Purpose
# Makes the words in a sentence scrambled

# Name: Bartek Kowalski
# Date: 2021-03-21


# importing random to change random letters later in the program
from random import randint

# Creating a list of punctuation so that we can check and remove punctuation so that it will not break our program
PUNCTUATION = [".", "?", "!", ",", ";", ":", "-", "(", ")", "[", "]", "{", "}", "\'", "\"", "*"]
punct = []
punctIndex = []
# Welcome
print("Welcome to my program! It scrambles a sentence that was inputted.")


# main function
def main():
    # Input sentence, with or without the punctuation
    sentence = input("Enter a sentence to be scrambled: ")
    storePunctuation(sentence)
    # calling the punctuation function to remove punctuation from the sentence
    sentencenopunct = punctuation(sentence)
    # calling the sentence split function to split the sentence into individual words.
    listsentence = sentenceSplit(sentencenopunct)
    # calling the sentence random function to scramble the words in the sentence
    newSentence = sentenceRandom(listsentence)
    # calling the add punctuation function to add back the punctuation to the sentence.
    final = addPunctuation(newSentence)
    # join the given words into a single sentence and output it to the user.
    print(final)


# this function adds punctuation to the final sentence
def addPunctuation(newSentence):
    # join the sentence together
    join = ''.join(newSentence)
    # split the sentence into letters
    letters = list(join)
    # setting variables for iteration
    y = 0
    x = 0
    # for each letter:
    for i in letters:
        # if the index has an Punctuation assigned to it
        if y in punctIndex:
            # add back in the punctuation
            letters.insert(y, punct[x])
            # increment variables
            y += 1
            x += 1
        else:
            # increment for looping
            y += 1
    # make the list a single sentence again
    final = ''.join(letters)
    # return the final string
    return final


# store punctuation function, stores the index and type of punctuation
def storePunctuation(sentence):
    # takes the input and turns it into a list
    list1 = list(sentence)
    # setting y equal to 0 for the loop
    y = 0
    # for each character in the list
    for i in list1:
        # if the character is in the punctuation list
        if i in PUNCTUATION:
            # store the type of punctuation and the index of it
            punct.append(i)
            punctIndex.append(y)
            # increment y by one
            y += 1
        # if it is not in the punctuation list:
        else:
            # increment y by one
            y += 1


# function that removes the punctuation from the sentence inputted
def punctuation(sentence):
    # defining lists that we can store final sentence in.
    sentencenopunct1 = []
    # split the sentence into individual words.
    words = sentence.split()
    # for each word in the array
    for word in words:
        # changes the word into a list of individual characters
        wordarray = list(word)
        i = 0
        # for each character in the word
        while i < len(wordarray):
            # if the character we are looping is in the punctuation array which was defined at the
            # beginning of the program, remove the character from the array.
            if wordarray[i] in PUNCTUATION:
                # no need to increment by one as the list will shift over one as a character was removed.
                wordarray.remove(wordarray[i])
            else:
                # increment i by one to move onto next character
                i += 1
        # join the letters together into a single word
        newWord = ''.join(wordarray)
        # add a space at the end of the word so that when words are appended into one sentence
        # they will have spaces between them.
        newWord2 = newWord + " "
        # add each word to a list
        sentencenopunct1.append(newWord2)
    # make the list into a single sentence.
    sentencenopunct = ''.join(sentencenopunct1)
    # return the sentence without punctuation
    return sentencenopunct


# function which splits a sentence into separate words
def sentenceSplit(sentence):
    # split the sentence
    x = sentence.split()
    # return the split sentence.
    return x


let2 = int


# function that figures out which letters to scramble.
def sentenceRandom(listsentence):
    # defining variables for looping, as well as list for scrambled words
    newlist = []
    x = 0
    # for each word:
    for i in listsentence:
        # if the length of the word in greater than 3:
        if len(listsentence[x]) > 3:
            # select the first character to swap (not the first or last)
            let1 = randint(1, len(listsentence[x]) - 2)
            redo = True
            while redo:
                # select the second character to swap (not the first or last)
                let2 = randint(1, len(listsentence[x]) - 2)
                # checking that they are not the same index
                if let2 != let1:
                    redo = False
            # checking if the characters that were chosen are not the same. This would
            # result in the word not changing, which we would not want.
            if i[let1] == i[let2] and len(i) != 4:
                # calling the check function, getting new values to swap if needed
                let1, let2 = check(let1, let2, i)
            # calling the replace function to replace the letters in the word.
            new = replace(let1, let2, i)
            # add the scrambled word into the newlist.
            newlist.append(new + " ")
        # if the length of the word is less than 3:
        else:
            # enter the word int the new list
            newlist.append(listsentence[x] + " ")
        # increment x by one
        x += 1
    # return the list with the new scrambled words
    return newlist


# check function, makes sure that the word has been scrambled if possible
def check(let1, let2, i):
    # set redo equal to true for the loop
    redo = True
    while redo:
        # if the characters that are going to be exchanged are not the same:
        if i[let1] != i[let2]:
            # return the characters
            return let1, let2
        # if the characters are the same:
        else:
            # Find a new random integer
            let2 = randint(1, len(i) - 2)


# replace function, replaces the letters of the word
def replace(let1, let2, i):
    # setting y equal to 0 for the loop
    y = 0
    # setting variables equal to the characters we need to replace
    num1 = i[let1]
    num2 = i[let2]
    # change the word into a list of characters that we can loop through
    listword = list(i)
    # for each letter in the list
    for x in listword:
        # if the character we are looping through is one of the characters we need to replace:
        if y == let1:
            # remove the letter we need to replace
            listword.remove(listword[y])
            # add the new character in its place
            listword.insert(y, num2)
        elif y == let2:
            # remove the letter we need to replace
            listword.remove(listword[y])
            # add the new character in its place
            listword.insert(y, num1)
        # increment y by one
        y += 1
    # join the word back together
    a = ''.join(listword)
    # return the scrambled word.
    return a


# calling main function
main()

# end
print("Thank you for using my program!")
