class Node:
    def __init__(self, data: str, next_node: "Node" = None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    # TODO: Do generalizing naming of function

    def __init__(self, head_node: Node):
        self.head_node = head_node

    def get_size(self) -> int:
        size: int = 0
        current_node: Node = Node(None, None)

        if self.head_node == None:
            return size
        else:
            current_node = self.head_node
            size += 1

        while current_node.next_node != None:
            current_node = current_node.next_node
            size += 1

        return size

    def append(self, new_node: Node):
        current_node: Node = self.head_node

        while current_node.next_node != None:
            current_node = current_node.next_node

        current_node.next_node = new_node

    def prepend(self, new_node: Node):
        new_node.next_node = self.head_node
        self.head_node = new_node

    def insert_node_by_index(self, index, new_node: Node):
        current_node: Node = self.head_node
        previous_node: Node = Node(None, None)
        for _ in range(index):
            previous_node = current_node
            current_node = current_node.next_node

        previous_node.next_node = new_node
        new_node.next_node = current_node

    def delete_node_by_index(self, index):
        current_node: Node = self.head_node
        previous_node: Node = Node(None, None)
        for _ in range(index):
            previous_node = current_node
            current_node = current_node.next_node

        previous_node.next_node = current_node.next_node

    def clear(self):
        self.head_node = None

    def get_node_by_index(self, index: int) -> Node:
        if index == 0:
            return self.head_node
        else:
            current_node: Node = self.head_node
            for _ in range(index):
                current_node = current_node.next_node

            return current_node

    def get_index_by_searching(self, searching_keyword: str) -> int:
        index: int = 0
        current_node: Node = self.head_node

        if self.get_size() == 0:
            if current_node.data == searching_keyword:
                return index
        else:
            while current_node.next_node != None:
                if current_node.data == searching_keyword:
                    return index
                else:
                    current_node = current_node.next_node
                    index += 1

        # If searching_keyword isn't existed in the linked list
        return -1
