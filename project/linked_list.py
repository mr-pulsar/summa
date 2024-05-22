from Nodefile import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_node(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)


    def display(self):
        cur = self.head
        while cur:
            print(cur.data , end = "->")
            cur = cur.next
        

    def delete_at_begin(self):
        if self.head is None:
            print("List is empty, nothing to delete")
        else:
            self.head = self.head.next
    