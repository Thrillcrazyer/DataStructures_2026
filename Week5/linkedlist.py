from node import DNode

class LinkedList:
    def __init__(self):
        self.head = DNode("head")
        self.tail = DNode("tail",prev_node=self.head)
        self.head.set_next(self.tail)
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.size == 0:
            return "[]"
        else:
            result = "["
            current = self.head.get_next()
            while current != self.tail:
                result += "{" + str(current) + "} ,"
                current = current.get_next()
            result = result[:-2] + "]"
            return result
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        """Accessor 1 first
        """
        if self.is_empty():
            raise IndexError("List is empty")
        return self.head.get_next()
    
    def last(self):
        """Accessor 2 last
        """
        if self.is_empty():
            raise IndexError("List is empty")
        return self.tail.get_prev()
    
    def prev(self, node:DNode):
        """Accessor 3 prev
        """
        if node == self.head:
            raise IndexError("No previous node for head")
        return node.get_prev().element
    
    def next(self, node:DNode):
        """Accessor 4 next
        """
        if node == self.tail:
            raise IndexError("No next node for tail")
        return node.get_next().element
    
    def replace(self, node:DNode, element):
        """Updater 1 replace
        """
        if node == self.head or node == self.tail:
            raise IndexError("Cannot replace head or tail")
        
        old_element = node.element
        node.set_element(element)
        return old_element
    
    def insert_after(self, node:DNode, element):
        """Updater 2 insertAfter
        """
        if node == self.tail:
            raise IndexError("Cannot insert after tail")
        
        new_node = DNode(element, prev_node=node, next_node=node.get_next())
        node.get_next().set_prev(new_node)
        node.set_next(new_node)
        
        self.size += 1
    
    def insert_before(self, node:DNode, element):
        """Updater 3 insertBefore
        """
        if node == self.head:
            raise IndexError("Cannot insert before head")
        
        new_node = DNode(element, prev_node=node.get_prev(), next_node=node)
        node.get_prev().set_next(new_node)
        node.set_prev(new_node)
        
        self.size += 1
    
    def remove(self, node:DNode):
        """Updater 4 remove
        """
        if node == self.head or node == self.tail:
            raise IndexError("Cannot remove head or tail")
        
        node.get_prev().set_next(node.get_next())
        node.get_next().set_prev(node.get_prev())
        
        self.size -= 1


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_after(linked_list.head, "난 Real 한 것만 뱉어서")
    linked_list.insert_after(linked_list.head.get_next(), "개명 신청 했어")
    linked_list.insert_before(linked_list.tail, "김진짜")
    
    print(f"{'1. Linked List insertions test':-<80}")
    # Output: [{Prev: head -> DNode(Element: 난 Real 한 것만 뱉어서) -> Next: 개명 신청 했어} ,{Prev: 난 Real 한 것만 뱉어서 -> DNode(Element: 개명 신청 했어) -> Next: 김진짜} ,{Prev: 개명 신청 했어 -> DNode(Element: 김진짜) -> Next: tail}]
    print(linked_list)
    print("-" * 80)
    print("\n")
    print(f"{'2. Linked List accessors test':-<80}")
    print(linked_list.first())  # Output: 난 Real 한 것만 뱉어서
    print(linked_list.last())   # Output: 김진짜
    print("LENGTH:", len(linked_list))  # Output: 3
    print("-" * 80)
    print("\n")
    print(f"{'3. Linked List remove/replace test':-<80}")
    linked_list.replace(linked_list.tail.get_prev(), "김가짜")
    print(linked_list)  # Output: [난 Real 한 것만 뱉어서 개명 신청 했어 김가짜]
    linked_list.remove(linked_list.head.get_next())
    print(linked_list)  # Output: [난 Real 한 것만 뱉어서 김가짜]
    print("LENGTH:", len(linked_list))  # Output: 2
    print("-" * 80)
    print("\n")
    
    print(f"{'4. Error handling test':-<80}")
    
    # empty list errors
    empty_list = LinkedList()
    try:
        empty_list.first()
    except IndexError as e:
        print(f"first() on empty list: {e}")
    try:
        empty_list.last()
    except IndexError as e:
        print(f"last() on empty list: {e}")
    # head/tail boundary errors
    try:
        linked_list.prev(linked_list.head)
    except IndexError as e:
        print(f"prev(head): {e}")
    try:
        linked_list.next(linked_list.tail)
    except IndexError as e:
        print(f"next(tail): {e}")
    try:
        linked_list.insert_after(linked_list.tail, "test")
    except IndexError as e:
        print(f"insert_after(tail): {e}")

    try:
        linked_list.insert_before(linked_list.head, "test")
    except IndexError as e:
        print(f"insert_before(head): {e}")
    
    try:
        linked_list.replace(linked_list.head, "test")
    except IndexError as e:
        print(f"replace(head): {e}")
    
    try:
        linked_list.replace(linked_list.tail, "test")
    except IndexError as e:
        print(f"replace(tail): {e}")
    
    try:
        linked_list.remove(linked_list.head)
    except IndexError as e:
        print(f"remove(head): {e}")

    try:
        linked_list.remove(linked_list.tail)
    except IndexError as e:
        print(f"remove(tail): {e}")
    print("-" * 80)
    