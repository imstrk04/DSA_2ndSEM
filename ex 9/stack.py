class Stack:
    def __init__(self):
        '''
            Constructor to initialise a list
        '''
        self.item = []
    
    def isempty(self):
        '''
            Method to check if stack is empty or not.
        '''
        return len(self.item) == 0
    
    def push(self, ele):
        '''
            Method to append element to a stack.
        '''
        self.item.append(ele)
    
    def pop(self):
        '''
            Method to remove elements from stack.
        '''
        return self.item.pop()

    def __len__(self):
        '''
            Method to return length of the stack.
        '''
        return len(self.item)
    
    def __str__(self):
        '''
            Overiding to print string value of the object.
        '''
        return str(self.item)

    def topelement(self):
        '''
            Method that returns the top value of the stack.
        '''
        return self.item[-1]