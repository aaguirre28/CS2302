"""
Alexis Aguirre
CS2302: Lab 2, Option B (Passwords)
Due on: 10/18/18
Lab goes over linked list practices by storing a set of 10 million
passwords in a linked list and then sorting in descending order by
repetition to find the 20 most common passwords.
"""
import sys
from pathlib import Path


def main():
#    usersFile = Path("C:/Users/aagui/Documents/UTEP 6th Semester/CS2302 Data Structures/Lab 2/10-million-combos.txt")       # File path with slashes edited, may be different on different OS
    usersFile = Path("10-million-combos.txt")       # 10 million passwords text file on same directory as main code 
    f = open(usersFile, 'r')    # Reading from file
    currLine = f.readline()
  #  while currLine != '':          # Solution A
    count = 0
    while count < 1000:             # checking algorithm with specific number for quick check
        count += 1
        currLine = currLine.strip()     #Stripping newline characters to avoid errors when checking passwords, and then splitting seperating data in file
        lineElements = currLine.split()
        if len(lineElements) == 2:      # Not considering empty passwords
            checkNode(passwords.head, Node(lineElements[1], 1, None))
        currLine = f.readline()
        
#    while currLine != '':           # Solution B
#    while count < 1000:             # checking algorithm with first 1000 for quick check
#        currLine = currLine.strip()     # Stripping newline characters to avoid errors when checking passwords, and then splitting seperating data in file
#        lineElements = currLine.split()
#        if len(lineElements) == 2:
#            checkNodeDict(Node(lineElements[1], 1, None))
#        currLine = f.readline()
#        count += 1
#    print(dict)

    swap = bubbleSort(passwords)    # Implementing bubble sort repeatedly until no swaps occur
    while swap == 1:
        swap = bubbleSort(passwords)

    tempNode = passwords.head          #Used to validate that linked list creation was correct
    printCount = 0
    while printCount < 20:              # Only printing 20 after sorting to find 20 most common passwords
#    while tempNode != None:         
        print(tempNode.password, end = ' ')
        print(tempNode.count, end = ' ')
        tempNode = tempNode.next
        printCount += 1

def bubbleSort(passwords):
    currNode = passwords.head
    nextNode = currNode.next
    tempPassword = ""
    tempCount = 0
    swap = 0
    while nextNode != None:
        if currNode.count < nextNode.count:         # Only password and count data are swapped if needed to
            tempPassword = nextNode.password
            tempCount = nextNode.count
            nextNode.password = currNode.password
            nextNode.count = currNode.count
            currNode.password = tempPassword
            currNode.count = tempCount
            swap = 1
        currNode = currNode.next
        nextNode = currNode.next
    return swap

def checkNode(currNode, newNode):       # Used for checking for repeated passwords in linked list
    while currNode != None:
        if currNode.password == newNode.password:
            currNode.count += 1         # Count incremented if repeated password
            return
        currNode = currNode.next
    passwords.addNode(newNode)          # Node added if new password

def checkNodeDict(newNode):         # Dict method used in solution b
    if newNode.password in dict:
        dict[newNode.password] += 1
    else:
        dict[newNode.password] = 1
        passwords.addNode(newNode)

class Node:
    password = ""
    count = -1
    next = None

    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next

class LinkedList:               # Linked list class to facilitiate linked list creation
    def __init__(self):
        self.head = None
        self.tail = None
    def addNode(self, newNode):
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

passwords = LinkedList()
dict = {}
main()