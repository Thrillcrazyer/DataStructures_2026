class DNode:
    def __init__(self, element, prev_node=None, next_node=None):
        self.element = element
        self.next = next_node
        self.prev = prev_node
        
    def __str__(self):
        return f"Prev: {self.prev.element if self.prev else None} -> DNode(Element: {self.element}) -> Next: {self.next.element if self.next else None}"
    
    def set_prev(self, prev_node):
        self.prev = prev_node
    
    def get_prev(self):
        return self.prev
    
    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next
    
    def set_element(self, element):
        self.element = element
        
    
if __name__ == "__main__":
    node1 = DNode("침착한")
    node2 = DNode("조준 방아쇠 소리는")
    node3 = DNode(" Tik Tock")
    
    node1.set_next(node2)
    node2.set_prev(node1)
    
    node2.set_next(node3)
    node3.set_prev(node2)
    
    print(node1)
    print(node2)
    print(node3)