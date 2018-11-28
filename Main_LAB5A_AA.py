"""
Alexis Aguirre
CS2302: Lab 5, Option A 
Due on: 11/27/18

"""
from HeapImplementation import Heap

def main():
    h = Heap()  # Create a heap object
    input_list = [ [10, 2, 5, 18, 22, 15, 12, 31, 50, 42, 38, 1, 29, 20, 76, 80, 3],
                  [71, 112, 118, 6, 20, 2, 12, 125, 151, 25, 54, 1, 100, 95, 81, 17, 26, 34, 47, 49, 13, 64, 77],
                  [4, 5, 12, 1, 20, 45, 13] ]       # 3 sets to test heap implementation
    
    for group in range(len(input_list)):    # for loop executes for each set in input list of lists
        print('New Set')
        for item in input_list[group]:      # insert each item into heap
            h.insert(item)
        count = 1           # counts used to print heap in a way you can visualize
        next_count = count * 2      # Counts will print each generation on the same line
        for item in h.heap_array:   # Will print all items in the heap
            print(item, end = ' ')
            count -= 1      # Count is decremented to keep track of generation
            if count == 0:      # When count reaches 0, you are done printing a generation
                print()         # Print newline, before updating counts for next generation
                count = next_count
                next_count = count * 2
        print('\nHeapsort Implementation')
        h.heapsort()        # Calls method for heap sort
                            # Heapsort method already has print instructions
        print('\n\n\n')     # Spacing between 
        
        
main()