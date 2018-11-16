"""
Alexis Aguirre
CS2302: Lab 4, Option B (English Word - Hash Tables)
Due on: 11/11/18

"""
import sys
from pathlib import Path

def main():
    hash_table_size = 750000            # Size for hash table
    words_table = ChainingHashTable(hash_table_size)         # Initializing hash table
    
    users_file = Path("words.txt")      # Identifying words file
    reader = open(users_file, 'r')      # Configuring reader
    current_line = reader.readline()
    
#    count = 0          # Count for debug purposes
#    while count != 100000:
#        count += 1        
    while current_line != '':       # While you are not at end of file
        word = current_line.strip()     # Lines stripped of leading/trailing white space
        word = word.lower()             # Words are made all lowercase before inserted
        words_table.insert(word)
        current_line = reader.readline()         # Move to next line

    print(words_table.search('search'), end = ' ')              # Test cases
    print(words_table.search('tungsten'), end = ' ')
    print(words_table.search('incredible'), end = ' ')
    print(words_table.search('increible'), end = ' ')
    print(words_table.search('amazing'), end = ' ')
    print(words_table.search('cocina'), end = ' ')
    print(count_anagrams(words_table, 'post'))
    print(count_anagrams(words_table, 'stale'))
    
def get_value(word):
    sorted_word = sorted(word)          # Sorts characters in alphabetical order
    power = len(sorted_word) - 1        # Greatest power of 26 that will be reached based on length of word
    hash_value = 0      # initialize hash value
    for i in range(len(sorted_word)):       # Calculates base 26 number off of word
        if sorted_word[i].isalpha() == False:       # If a character is not a letter, return -1, not valid word, maybe a combined word
            return -1
        hash_value += (ord(sorted_word[i]) - 97) * (26**power)
        power -= 1
        
    return hash_value

def count_anagrams(words_table, word):
    anaList = []
    check_anagrams(anaList, words_table, word)     # List populated with anagrams
#    print(word, end = ' ')             # Print for debugging
#    print(len(anaList), end = ' ')
    return len(anaList)         # Anagram Count is returned

def check_anagrams(anaList, words_table, word, prefix = ""):
    if len(word) <= 1:
        str = prefix + word        
        if words_table.search(str) != False:
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
                check_anagrams(anaList, words_table, before + after, prefix + cur)
     
class ChainingHashTable:
    
    def __init__(self, table_size):
        self.table = [] 
        for i in range(table_size):
            self.table.append([])
        
    def insert(self, word):
        bucket = get_value(word) % len(self.table)
        if bucket != -1:        # Invalid words will return -1 as a hash value, meaning they are not in hash table
            bucket_list = self.table[bucket]
            bucket_list.append(word)
            
    def search(self, word):
        bucket = get_value(word) % len(self.table)
        bucket_list = self.table[bucket]
        if word in bucket_list:
            return True
        return False
     
main()