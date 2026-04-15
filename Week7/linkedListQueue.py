from linkedlist import LinkedList

class LQueue:
    def __init__(self):
        self.front = None
        self.data = LinkedList()
        
    def __str__(self):
        string =''
        string += "There are " + str(self.size()) + " elements: "
        string += str(self.data) 
        return string
    
    def enqueue(self, element):
        if self.front is None:
            self.front = self.data.insert_after(self.data.head, element)
        else:
            self.data.insert_after(self.data.tail.get_prev(), element)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        node = self.front
        self.front = node.get_next()
        
        if self.front == self.data.tail:
            self.front = None
        return self.data.remove(node)

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


if __name__=='__main__':
    q=LQueue()
    q.enqueue("김채원")
    print(q)
    q.enqueue("백지헌")
    print(q)
    q.dequeue()
    print(q)
    q.enqueue("배혜림")
    print(q)