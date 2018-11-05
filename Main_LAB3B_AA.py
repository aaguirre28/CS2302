"""
Alexis Aguirre
CS2302: Lab 3, Option B (Passwords)
Due on: 11/4/18

"""
import sys
from pathlib import Path
from AVLTree import Node, AVLTree
from RedBlackTree import RBTNode, RedBlackTree

def main():
    usersFile = Path("words.txt")
    f = open(usersFile, 'r')    # Reading from file
    currLine = f.readline()
    
    print('Are you creating an AVL tree, or a red-black tree?')
    print('Type "A" and press ENTER for AVL Tree.')
    print('Type "B" and press ENTER for red-black tree.')
    
    treeChoice = input()

    if treeChoice == 'A':
        print('Creating and populating AVL tree with english words ...')
        engish_words = AVLTree()
        count = 0
        while currLine != '':          # AVL Tree Solution
            count += 1
            if count%10000 == 0:         # Progress check for debugging
                print(count, end = ' ')
#                print(currLine, end = ' ')
            currLine = currLine.strip()     #Stripping newline characters to avoid errors when checking passwords, and then splitting seperating data in file
            currLine = currLine.lower()
            engish_words.insert(Node(currLine))
            currLine = f.readline()    
#        testNode = engish_words.search('Zurkow')           # Test code for debugging
#        print(testNode.key)

    elif treeChoice == 'B':
        print('Creating and populating red-black tree with english words ...')
        engish_words = RedBlackTree()
        count = 0
        while currLine != '':           # Red Black Tree Solution
            count += 1
            if count%10000 == 0:         # Progress Check for debugging
                print(count, end = ' ')
#                print(currLine, end = ' ')
            currLine = currLine.strip()
            currLine = currLine.lower()
            engish_words.insert(currLine)   # Unlike AVL Tree, red black tree  
            currLine = f.readline()
#        testNode = engish_words.search('unpollened')        # Test code for debugging
#        print(testNode.key)
    
    else:
        print('Invalid input.')
        return

    print(count_anagrams(engish_words, "spot"))    # Test anagram count function   
    print(count_anagrams(engish_words, "late"))    
    
    print(max_anagram('anagram_words.txt', engish_words))   # Test max_anagram function
    

def max_anagram(filePath, engish_words):
    usersFile = filePath        
    f = open(usersFile, 'r')    # Reading from file
    currLine = f.readline()
    words = []
    while currLine != '':
        currLine = currLine.strip()     #Strip blank spaces from words
        currLine = currLine.lower()     # Bring everything to lowercase to avoid losing words
        words.append(currLine)
        currLine = f.readline()
    maxAnagram = ''
    for i in range(len(words)):
        if(i == 0):
            maxAnagram = words[0]       # Sets initial
            maxAnagramCount = count_anagrams(engish_words, words[0])    
        elif(count_anagrams(engish_words, words[i]) > maxAnagramCount):     # Changes if greater than previous
            maxAnagram = words[i]
            maxAnagramCount = count_anagrams(engish_words, words[i])
    return maxAnagram

def count_anagrams(engish_words, word):
    anaList = []
    check_anagrams(anaList, engish_words, word)     # List populated with anagrams
#    print(word, end = ' ')             # Print for debugging
#    print(len(anaList), end = ' ')
    return len(anaList)         # Anagram Count is returned

def check_anagrams(anaList, engish_words, word, prefix = ""):
    if len(word) <= 1:
        str = prefix + word        
        testNode = engish_words.search(str)
        if testNode != None:
#            print(prefix + word, end = ' ')     # Print for debugging
            anaList.append(str)         # Added to list if anagram
#        if str in engish_words:        # Orig code
#            print(prefix + word)
    
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]     # letters before cur
            after = word[i + 1:]    # letters after cur
            
            if cur not in before:   # Check if permutations of cur have not been granted
                check_anagrams(anaList, engish_words, before + after, prefix + cur)
    

main()

