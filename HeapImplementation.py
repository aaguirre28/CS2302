class Heap:
    
    def __init__(self):         # Heap initialization
        self.heap_array = []

    def insert(self, k):        
        self.heap_array.append(k)       # After appending, heap needs to be reorganized
        self.percolate_up(len(self.heap_array) - 1)     # Percolating appended item up
        # TODO: Complete implementation

    def extract_min(self):
        if self.is_empty():     # If empty, there is no min to extract
            return None
        min_elem = self.heap_array[0]       # Minimum element is always at first index
        self.heap_array[0] = self.heap_array[len(self.heap_array) - 1]      # Swap with last element
        self.heap_array.pop()       # Pop last element, since method already saved it in variable
        if not self.is_empty():     # After popping, you need to reorganize heap 
            self.percolate_down(0)            
        # TODO: Complete implementation
        return min_elem         # You get minimum element returned to you

    def is_empty(self):     # Boolean determined by length of array
        return len(self.heap_array) == 0    # if array is empty, length is 0, then true is returned

    def percolate_up(self, current_index):
        while current_index > 0:    # If current index is 0, you can't percolate up any further. 
            parent_index = (current_index - 1) // 2     # Formula given to us before to get parent indices
            if self.heap_array[current_index] >= self.heap_array[parent_index]:     # If satisfied, heap is already correctly organized
                return
            else:
                temp = self.heap_array[current_index]       # Swap is carried out if current element is less than parent element
                self.heap_array[current_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                
                current_index = parent_index        # Index being tested is updated
        
    def percolate_down(self, current_index):
        child_index = 2 * current_index + 1     # for percolate down you are given parent index, and need children indices
        current_value = self.heap_array[current_index]      # Save element for comparisons later
        
        while child_index < len(self.heap_array):   # Children must exist in heap, don't want out of index errors
            min_value = current_value       # Setting current element to minimum
            min_index = -1
            child_count = 0         # Child count used to access both children if two exist
            while child_count < 2 and child_count + child_index < len(self.heap_array):
                if self.heap_array[child_count + child_index] < min_value:      # If a child is less than parent, min value and index are updated
                    min_value = self.heap_array[child_count + child_index]
                    min_index = child_count + child_index
                child_count += 1
                
            if min_value == current_value:  # If no update occurred, heap is already in correct organization
                return
            else:
                temp = self.heap_array[current_index]       # If parent was not smaller than children, swap with minimum occurs
                self.heap_array[current_index] = self.heap_array[min_index]
                self.heap_array[min_index] = temp
                
                current_index = min_index           # observed indices are updated. 
                child_index = 2 * current_index + 1
                
    def heapsort(self):
        while not self.is_empty():      # Since extract_min is already set up to pop and percolate heap, you just need that method
            print(self.extract_min(), end = ' ')        # Extract min, print, and move on to next element
            
