
class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self) -> None:
        node = self.head
        while node:
            yield node
            node = node.next
    # inserting a node in silngly linked list

    def insert(self, value, location):
        newnode = Node(value)
        if(self.head == None):
            self.head = newnode
            self.tail = newnode
        elif location == 0:
            newnode.next = self.head
            self.head = newnode
        elif location == -1:
            newnode.next = None
            self.tail.next = newnode
            self.tail = newnode
        else:
            tempNode = self.head
            index = 0

            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next

            newnode.next = nextNode
            tempNode.next = newnode

    # traverse singly linked list
    def traverseSLL(self):
        if self.head == None:
            print("SLL does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    # search sll

    def searchSLL(self, value):
        node = self.head
        index = 0
        if node == None:
            print('linked list not found')
        while node != None:
            if(node.value == value):
                print('index', index)
                break
            else:
                index += 1
                node = node.next
        else:
            print("the value does not exist in the list")

    def deleteSLL(self, location):
        node = self.head
        if self.head == None:
            print("no linked list so ever")
        elif(location == 0):
            if(self.head == self.tail):
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif(location == -1):
            if(self.head == self.tail):
                self.head = None
                self.tail = None
            while node is not None:
                if(node.next == self.tail):
                    break
                node = node.next
            node.next = None
            self.tail = node
        else:
            index = 0
            while index < location - 1:
                node = node.next
                index += 1
            nextNode = node.next
            node.next = nextNode.next


singleLinkedList = SingleLinkedList()
singleLinkedList.insert(2, 5)
singleLinkedList.insert(1, 0)
singleLinkedList.insert(6, -1)
singleLinkedList.insert(3, 2)
singleLinkedList.insert(4, 3)
singleLinkedList.insert(5, 4)

print([node.value for node in singleLinkedList])
singleLinkedList.traverseSLL()
singleLinkedList.searchSLL(7)

singleLinkedList.deleteSLL(3)
print([node.value for node in singleLinkedList])
