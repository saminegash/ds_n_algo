from linkedlist import LinkedList


def nthToLast(ll, n):
    pointer = ll.head
    pointer1 = ll.head
    for i in range(n):
        if pointer1 is None:
            return None
        pointer1 = pointer1.next

    while pointer1.next:
        pointer1 = pointer1.next
        pointer = pointer.next
    return {"nthtoLast": pointer.value, "last": pointer1.value, "n": n}


customLL = LinkedList()
customLL.generate(10, 0, 8)
print(customLL)
print(nthToLast(customLL, 3))
