class Queue:
    
    def __init__(self, maxsize=5):
        self.items = []
        self.maxsize = maxsize
        self.size = 0

    def enqueue(self, data):
        if self.size < self.maxsize:
            self.items.append(data)
            self.size+=1
            print self.items
        
    def dequeue(self):
        self.size-=1
        print self.items[0]
        del self.items[0]

    def insert(self, index, data):
        if self.size < self.maxsize:
            self.size+=1
            self.items.insert(index, data) 
            print self.items
            
def main():
    x = Queue(10)
    x.enqueue(2)
    x.enqueue(5)
    x.enqueue(7)
    x.enqueue(3)
    x.enqueue(4)
    x.dequeue()
    x.dequeue()
    x.insert(3,10)
    x.insert(1,1)

if __name__ == '__main__':
    main()

