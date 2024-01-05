class Queue:
    def __init__(self):
        '''
            Constructor to initialise variables.
        '''
        self.item = []
        self.front = 0
        self.rear = 0
    
    def isempty(self):
        '''
            Method to check if Queue is empty
        '''
        if self.front == self.rear:
            return True
        else:
            return False
    
    def enqueue(self, ele):
        '''
            Method to add elements to the queue.
        '''
        self.item.insert(self.rear, ele)
        self.rear += 1
    
    def dequeue(self):
        '''
            Methods to remove elements from the queue.
        '''
        return self.item.pop(0)
    
    def __len__(self):
        '''
            Method to return length of the queue.
        '''
        return self.rear - self.front
    
    def __str__(self):
        '''
            Overiding to return the string value of the object
        '''
        return str(self.item)