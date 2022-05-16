# question: You have two numbers represented by a linked list, where
# each node contains a single digit, the digits are stored in reverse order, such
# that the 1's digit is at the head of the list, Write a function that adds the two
# numbers and returns the sum as a linked list

from linkedlist import LinkedList, Node


def sumTwoLinkedList(lst1, lst2):
    num1 = 0
    num2 = 0

    lst1Head = lst1.head
    lst2Head = lst2.head
    index = 0
    while lst1Head:
        num1 += lst1Head.value * (10 ** index)
        index += 1
        lst1Head = lst1Head.next

    index = 0
    while lst2Head:
        num2 += lst2Head.value * (10 ** index)
        index += 1
        lst2Head = lst2Head.next
    total = num1 + num2
    ll = LinkedList()
    while total > 0:
        rem = total % 10
        total = total // 10
        node = Node(rem)
        if ll.head is None:
            ll.head = node
            ll.tail = node
        else:
            ll.tail.next = node
            ll.tail = node
    print(num1 + num2)
    return ll


def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    result = 0
    ll = LinkedList()
    while n1 or n2:

        if n1:
            result += n1.value
            n1 = n1. next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        result = result // 10
    ll.add(int(result % 10))

    return ll


customLL1 = LinkedList()
customLL2 = LinkedList()
customLL1.generate(3, 0, 9)
customLL2.generate(3, 0, 9)
print(customLL2)
print(customLL1)

print(sumTwoLinkedList(customLL1, customLL2))
print(sumList(customLL1, customLL2))
