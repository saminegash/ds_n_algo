import tarfile
from requests import head


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # creation of dll
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return 'the dll is created successfully'

    # insertion in dll
    def insertDLL(self, location, value):
        newNode = Node(value)
        if self.head == None:
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.tail = newNode
        elif location == 0:
            newNode.next = self.head
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode
        elif location == -1:
            newNode.next = None
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            if(tempNode == self.tail):
                newNode.next = self.tail.next
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    # traverse doubly linked list
    def traverseDLL(self):
        if self.head == None:
            print("SLL does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    # reverse traverse double linked list

    def reverseTraveseDLl(self):
        if self.tail == None:
            print("DLL does not exist")
        else:
            node = self.tail
            while node is not None:
                print(node.value)
                node = node.prev
    # searching in doubly linked list

    def searchDLL(self, value):
        index = 0
        if self.head is None:
            return "No list available"
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return node.value, index
                node = node.next
                index += 1
            return 'there is no value such value in a list'

    def deleteANodeDLL(self, location):
        if self.head is None:
            return "there is no list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curNode = self.head
                index = 0
                while index < location-1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
    # delete the entire doubly linked list

    def deleteDLL(self):
        currNode = self.head
        while currNode is not Node:
            currNode.prev = None
            currNode = currNode.next
        self.head = None
        self.tail = None


dll = DoublyLinkedList()
dll.createDLL(5)
dll.insertDLL(0, 3)
dll.insertDLL(-1, 6)
dll.insertDLL(2, 0)
dll.insertDLL(2, 8)
dll.insertDLL(-1, 7)
print([node.value for node in dll])
# dll.traverseDLL()
dll.reverseTraveseDLl()
print(dll.searchDLL(5))
dll.deleteANodeDLL(2)

print([node.value for node in dll])
