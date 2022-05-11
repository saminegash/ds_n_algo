class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None


class CircularDLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    # create circular double linked list

    def createCDLL(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode
        return "CDLL created successfully"
    # insertion of a new node in circular dll

    def insertCDLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            return "no list exist"
        elif(location == 0):
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.head = newNode
            self.tail.next = newNode
        elif(location == -1):
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.tail = newNode
        else:
            currNode = self.head
            index = 0
            while index < location-1:
                currNode = currNode.next
                index += 1

            newNode.next = currNode.next
            newNode.prev = currNode
            newNode.next.prev = newNode

            currNode.next = newNode

    def traverseCDLL(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if(node == self.tail.next):
                break

    def reversetraverseCDLL(self):
        if self.head is None:
            return "Circular doubly linked list does not exist"
        node = self.tail
        while node:
            print(node.value)
            node = node.next
            if(node == self.head.prev):
                break

    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "circulra dll does not exist"
        else:
            node = self.head
            index = 0
            while node:
                if node.value == nodeValue:
                    return node.value, index
                if node == self.tail:
                    return str(nodeValue) + " does not exist on circular dll"
                node = node.next
                index += 1

    def deleteNodeCDLL(self, location):
        if self.head is None:
            return "there is no node to delete"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head.next.prev = self.tail
                    self.tail.next = self.head.next
                    self.head.prev = None
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    prevTail = self.tail.prev
                    self.head.prev = prevTail
                    prevTail.next = self.head
                    self.tail = prevTail
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode

    def deleteCDLL(self):
        self.tail.next = None

        node = self.head
        while node:
            node.prev = None
            node = node.next
        self.head = None
        self.tail = None
        return "deletion of CDLL successful"


circularDLL = CircularDLL()
circularDLL.createCDLL(5)
print([node.value for node in circularDLL])

circularDLL.insertCDLL(4, 0)
circularDLL.insertCDLL(3, 0)
circularDLL.insertCDLL(2, 0)
circularDLL.insertCDLL(1, 0)
circularDLL.insertCDLL(7, -1)
circularDLL.insertCDLL(6, 4)

print([node.value for node in circularDLL])
