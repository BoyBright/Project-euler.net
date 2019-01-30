class Stack:

    def __init__(self, maxsize=5):
        self.items = []
        self.maxsize = maxsize
        self.size = 0

    def push(self, data):
        if isinstance(data, list):
            if self.size+len(data) <= self.maxsize:
                self.items.extend(data)
                self.size+=len(data)
        else:    
            if self.size < self.maxsize:
                self.items.append(data)
                self.size+=1
        print self.items        
        
    def pop(self):
        self.size-=1
        print self.items[-1]
        del self.items[-1] 
        

    def peek(self):
        print self.items[-1]    

def main():
    x = Stack(10)
    x.push(5)
    x.peek()
    x.push([6,1,9,7])
    x.pop()

if __name__ == '__main__':
    main()

