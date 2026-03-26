from dataclasses import dataclass

@dataclass
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        info="["
        while self.next is not None:
            info += str(self.value) + " -> "
            self = self.next
        info += str(self.value)
        info += "]"
        return info
a=Node(10)
b=Node(20)
a.next=b
print(a)