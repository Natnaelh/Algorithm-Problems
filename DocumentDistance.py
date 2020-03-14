#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:28:06 2019

@author: natnem
"""
import math
def main():
    filename1 = 'DocumentOne.txt'
    filename2 = 'DocumentTwo.txt'
    WordListOne = getListOfWords(filename1)
    WordListTwo = getListOfWords(filename2)
    WordFreqOne = countFreq(WordListOne)
    WordFreqTwo = countFreq(WordListTwo)
    res = Vector_Angle(WordFreqOne, WordFreqTwo)
    print ("The distance between the documents is: " ,res, "radians")
#    print(WordListOne)
def getListOfWords(filename):
    in_file = open(filename,'r')
    line = in_file.readlines()
    wordList = []
    charlist = []
    for strings in line:
        for chars in strings:
            if chars.isalnum():
                charlist.append(chars)
            elif len(charlist) > 0:
                word = "".join(charlist)
                word = word.lower()
                wordList.append(word)
                charlist = []
#    if len(charlist) > 0:
#                word = "".join(charlist)
#                word = word.lower()
#                wordList.append(word)

    return wordList
    

def countFreq(wordlist):
    word = {}
    for item in wordlist:
        if item not in word:
            word[item] = 1
        else:
            word[item] += 1
    return word
    

def Dot_Product(File1, File2):
    prod = 0
    for w in File1:
        if w in File2:
            prod += (File1[w]*File2[w])
    return prod

def Vector_Angle(L1 , L2):
    numerator  = Dot_Product(L1,L2)
    denominator  = math.sqrt(Dot_Product(L1,L1)*Dot_Product(L2,L2))
    return math.acos(numerator/denominator)
    
    
if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")

#
#def count_freq(wordlist):
#    L = []
#    for new_word in wordlist:
#        for entry in L:
#            if new_word == entry[0]:
#                entry[1] = entry[1] + 1
##                print(entry)
#                break
#        else:
#            L.append([new_word,1])
#    return L
#
#word_list = ["hello","my","name","is","natnael","habtamu","and","i","am","thankfull","for","all","the","things","God","did","for","me","happy"]
#print(count_freq(word_list))