class Stack:
    def __init__(self,d): #입력, 초기화
      self.top=-1
      self.dim=d
      self.data=[0]*d
      
    def __str__(self):
        string =''
        string += "There are " + str(self.size()) + " element: "
        string += '['
        for i in range(0, self.size()):
            if i==self.size()-1:
                string += str(self.data[i]) + ']'
            else:
                string += str(self.data[i]) + ', '
        return string

    def push(self, o):
      if(self.top==len(self.data)-1): #Stack이 가득 찬 경우
        self.data=self.data+[0]*self.dim #원하는 dimension만큼 늘려줌
      else:
        self.top=self.top+1
        self.data[self.top]=o

    def pop(self):
      if self.top<0:
        print("Stack is Empty")
        return None
      else:
        self.top=self.top-1
        return self.data[self.top]

    def isEmpty(self):
      if self.top<0:
        return True
      else:
        return False

    def size(self):
      return self.top+1
  

if __name__=='__main__':
  s=Stack(2)
  s.push("Gildong Hong")
  s.push("Sangmin Jo")
  s.pop()
  s.push("Gilsun Hong")
  s.pop()
  s.pop()
  s.push("Hyerim Bae")

  #print(s.top)

  print(s)