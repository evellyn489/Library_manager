class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, elemento): 
        new_node = Node(elemento)

        if self.head == None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = new_node
            new_node.previous = pointer
            new_node.next = None
        self.size += 1

    def remove(self, index: int): 
        if (index == 0):
            pointer = self.head
            if self.head.next != None:
                self.head = self.head.next
                self.head.previous = None
            else:
                self.head = None

            return pointer

        position = 1
        previous = self.head
        pointer = self.head.next
        while (position < index):
            previous = pointer
            pointer = pointer.next
            position = position + 1
        
        if (pointer.next != None):
            previous.next = pointer.next
            pointer.next.previous = pointer.previous
        else:
            previous.next = None
            pointer.previous = None

        self.size -= 1
        return pointer
        
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        pointer = self.head
        
        for i in range(index):
            if pointer != None:
                pointer = pointer.next
        return pointer.data

    def index(self, elemento):
        pointer = self.head
        index = 0

        while pointer != None:
            if pointer.data == elemento:
                return index
            pointer = pointer.next
            index += 1
    
    def __repr__(self):
        r = ''
        pointer = self.head

        while pointer != None:
            r += str(pointer.data) + '\n'
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()