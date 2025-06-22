from typing import Any, Optional

class Node:
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next
    
    def __str__(self) -> str:
        return 'Node[{value}]'.format(value=self.value)
    

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, elem: Any) -> None:
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, elem: Any) -> None:
        if self.head is None:
            return
        if self.head.value == elem:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == elem:
                current.next = current.next.next
                return
            current = current.next

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
