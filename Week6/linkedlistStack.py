from linkedlist import LinkedList

class LStack:
    def __init__(self):
        self.top = None
        self.data = LinkedList()
        
    def __str__(self):
        string =''
        string += "There are " + str(self.size()) + " element: "
        string += str(self.data) 
        return string
    
    def push(self, o):
        self.top = self.data.insert_before(self.data.tail, o)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        node = self.top
        self.top = node.get_prev()
        
        if self.top == self.data.head:
            self.top = None
        return self.data.remove(node)

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


if __name__=='__main__':
  s=LStack()
  s.push("김채원")
  print(s)
  s.push("백지헌")
  print(s)
  s.pop()
  print(s)
  s.push("배혜림")
  print(s)