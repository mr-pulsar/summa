from Nodefile import Node

class LinkedList:
    def __init__(self) -> None:
        pass

    def insert_node(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp:
                temp = temp.next
            temp.next = Node(data)


    def display(self):
        pass

    def delete_at_begin(self):
        pass
    
