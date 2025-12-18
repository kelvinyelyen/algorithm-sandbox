class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last

    def print_list(self, node):
        while(node is not None):
            print(node.data, end=" <-> ")
            node = node.next
        print("None")

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(6)
    dll.push(7)
    dll.push(1)
    dll.append(4)
    # 1 <-> 7 <-> 6 <-> 4 <-> None
    dll.print_list(dll.head)
