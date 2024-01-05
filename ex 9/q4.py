class PQueue:
    def __init__(self):
        '''
            Constructor to initialise two lists.
        '''
        self.hpq = []
        self.lpq = []
    
    def enqueue(self, priority, ele):
        '''
            Adding elements to the 2 queues depeding on the priority value.
        '''
        if priority == 0:
            self.hpq.append(ele)
        elif priority == 1:
            self.lpq.append(ele)
        else:
            raise ValueError("Invalid Priority.")

    def dequeue(self):
        '''
            Deleting elements from the queue depending on the priority value.
        '''
        if self.hpq:
            return self.hpq.pop(0)
        elif self.lpq:
            return self.lpq.pop(0)
        else:
            raise IndexError("Pqueue is empty. Can't dequeue further.")
    
    def isempty(self):
        '''
            Checking if the high priority queue and low priority queue are empty
        '''
        return len(self.hpq) == 0 and len(self.lpq)  == 0

if __name__ == "__main__":
    pq = PQueue()

    pq.enqueue(0, "Sada")
    pq.enqueue(1, "Kopa")

    print(pq.dequeue())

    pq.enqueue(1, "Rama")
    pq.enqueue(0,"Krishnan")

    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())