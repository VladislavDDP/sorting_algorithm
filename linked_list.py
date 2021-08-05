class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class List:
    def __init__(self) -> None:
        self.head = None

    def add_item(self, value) -> None:
        if self.head is None:
            self.head = Node(value, None)
        else:
            node = Node(value, self.head)
            self.head = node

    def remove_item(self, value) -> None:
        pass

    def print_items(self) -> None:
        node = self.head
        while node:
            print(node.value)
            node = node.next


list = List()
list.add_item(1)
list.add_item(2)
list.add_item(3)
list.add_item(4)

print('Printing items from the list: ')
list.print_items()
