
class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class CircularSLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self) -> None:
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # create circular linked list
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"
    # inserting a node in silngly linked list

    def insert(self, value, location):
        newnode = Node(value)
        if(self.head == None):
            self.head = newnode
            self.tail = newnode
            self.head.next = newnode
        elif location == 0:
            newnode.next = self.head
            self.head = newnode
            self.tail.next = newnode
        elif location == -1:
            newnode.next = self.head
            self.tail.next = newnode

            self.tail = newnode
        else:
            tempNode = self.head
            index = 0

            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            if(self.tail == tempNode):
                self.tail = newnode

            newnode.next = nextNode
            tempNode.next = newnode

    # traverse singly linked list
    def traverseCSLL(self):
        if self.head == None:
            print("CSLL does not exist")
        else:
            node = self.head
            index = 0
            while index >= 0:
                print(node.value)
                node = node.next
                if(index > 0 and node == self.head):
                    break
                index += 1
    # search sll

    def searchCSLL(self, value):
        node = self.head
        index = 0
        if node == None:
            print('linked list not found')
        while node:
            if(node.value == value):
                return node.value, index
            node = node.next
            index += 1
            if node == self.tail.next:
                return 'node does not exist in the csll'

    def deleteCSLL(self, location):
        node = self.head
        if self.head == None:
            print("no linked list so ever")
        elif(location == 0):
            if(self.head == self.tail):
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif(location == -1):
            if(self.head == self.tail):
                self.head.next = None
                self.head = None
                self.tail = None

            while node is not None:
                if(node.next == self.head):
                    break
                node = node.next
            node.next = self.head
            self.tail.next = None
            self.tail = node
        else:
            index = 0
            while index < location - 1:
                node = node.next
                index += 1
            nextNode = node.next
            node.next = nextNode.next

    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None


cSLL = CircularSLL()
cSLL.createCSLL(1)
# cSLL.insert(2, 5)
cSLL.insert(1, 0)
cSLL.insert(6, -1)
# cSLL.insert(3, 2)
cSLL.insert(4, 3)
# cSLL.insert(5, 4)
print(cSLL.tail.next.value)
print([node.value for node in cSLL])
cSLL.traverseCSLL()
# cSLL.traverseSLL()
print(cSLL.searchCSLL(7))

cSLL.deleteCSLL(3)
print([node.value for node in cSLL])
cSLL.traverseCSLL()
