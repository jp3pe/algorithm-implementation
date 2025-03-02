class Node:
    def __init__(self, data: str, next_node: "Node" = None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node: Node = None):
        self.head_node = head_node

    def get_size(self) -> int:
        size: int = 0
        current_node: Node = self.head_node

        while current_node:
            size += 1
            current_node = current_node.next_node

        return size

    def append(self, new_node: Node):
        if not self.head_node:
            self.head_node = new_node
            return

        current_node: Node = self.head_node
        while current_node.next_node:
            current_node = current_node.next_node

        current_node.next_node = new_node

    def prepend(self, new_node: Node):
        new_node.next_node = self.head_node
        self.head_node = new_node

    def insert_node_by_index(self, index: int, new_node: Node):
        if index == 0:
            self.prepend(new_node)
            return

        current_node: Node = self.head_node
        for _ in range(index - 1):
            if not current_node.next_node:
                raise IndexError("Index out of bounds")
            current_node = current_node.next_node

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def delete_node_by_index(self, index: int):
        if index == 0:
            if not self.head_node:
                raise IndexError("Index out of bounds")
            self.head_node = self.head_node.next_node
            return

        current_node: Node = self.head_node
        for _ in range(index - 1):
            if not current_node.next_node:
                raise IndexError("Index out of bounds")
            current_node = current_node.next_node

        if not current_node.next_node:
            raise IndexError("Index out of bounds")
        current_node.next_node = current_node.next_node.next_node

    def clear(self):
        self.head_node = None

    def get_node_by_index(self, index: int) -> Node:
        current_node: Node = self.head_node
        for _ in range(index):
            if not current_node:
                raise IndexError("Index out of bounds")
            current_node = current_node.next_node

        if not current_node:
            raise IndexError("Index out of bounds")
        return current_node

    def get_index_by_searching(self, search_keyword: str) -> int:
        index: int = 0
        current_node: Node = self.head_node

        while current_node:
            if current_node.data == search_keyword:
                return index
            current_node = current_node.next_node
            index += 1

        return -1
