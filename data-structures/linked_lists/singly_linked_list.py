class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ➝  ')
            current = current.next
        print(None)

    def insert_at(self, index, data):
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_at(self, index):
        if index < 0:
            raise IndexError("Index must be a non-negative integer.")
        
        if self.head is None:
            raise IndexError("Cannot delete from an empty list.")
        
        # Deleting the head node
        if index == 0:
            self.head = self.head.next
            return
        
        # Traverse to the node just before the target
        current = self.head
        for i in range(index - 1):
            if current.next is None:  # If index is out of range
                raise IndexError("Index out of range.")
            current = current.next
        
        # If the next node is None, the index is invalid
        if current.next is None:
            raise IndexError("Index out of range.")
        
        # Update the pointer to skip the node at the given index
        current.next = current.next.next


# sll = SinglyLinkedList()
