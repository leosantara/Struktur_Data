class CircularQueue:
    def __init__(self,cap):
        self.data = list()
        self.size = 0
        self.capacity = cap
        self.front = -1
    def enqueue(self, d):
        while len(self.data) != self.capacity:
            self.data.append(None)
        while None in self.data :
            self.data.remove(None)
        self.data.append(d)
        self.size += 1
        self.front = 0
        while len(self.data) != self.capacity:
            self.data.append(None)
        b = 0
        for i in self.data :
            if i == None :
                b += 1
        if b == 0 :
            print("Antrian Penuh!")

    def dequeue(self):
        for i in self.data:
            if i == None :
                self.data.remove(self.data[i])
        if self.size > 0 :
            hasil = self.data[self.front]
            self.data.pop(self.front)
            self.size -= 1
            return hasil
        else :
            print("Kosong!")

    def __len__(self):
        return self.size
    
    def front(self):
        return self.data[self.front]
    
    def display(self):
        while None in self.data :
            self.data.remove(None)
        print("Yang ada pada antrian adalah : ", end ='')
        for d in self.data:
            print(d, " ", end='')
        

circularQueue = CircularQueue(5)
circularQueue.enqueue(14)
circularQueue.enqueue(22)
circularQueue.enqueue(13)
circularQueue.enqueue(-6)
circularQueue.display()
print("Data yang dihapus adalah = ", circularQueue.dequeue())
print("Data yang dihapus adalah = ", circularQueue.dequeue())
circularQueue.display()
circularQueue.enqueue(9)
circularQueue.enqueue(20)
circularQueue.enqueue(5)
circularQueue.display()