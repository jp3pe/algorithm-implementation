import unittest
from linked_list import Node, LinkedList


class TestLinkedList(unittest.TestCase):

    def test_get_size(self):
        # Create initial linked list with one node
        head_node_1 = Node(data="head")
        linked_list_1 = LinkedList(head_node=head_node_1)

        # Append new nodes
        linked_list_1.append(Node(data="node1"))
        linked_list_1.append(Node(data="node2"))

        # Check the size of the linked list
        self.assertEqual(linked_list_1.get_size(), 3)

        # Test for the empty linked list
        linked_list_2 = LinkedList(None)
        self.assertEqual(linked_list_2.get_size(), 0)

    def test_append(self):
        # Create initial linked list with one node
        head_node = Node(data="head")
        linked_list = LinkedList(head_node=head_node)

        # Append new node
        new_node = Node(data="new_node")
        linked_list.append(new_node)

        # Check if the new node is appended correctly
        self.assertEqual(linked_list.head_node.next_node.data, "new_node")

    def test_prepend(self):
        # Create initial linked list with one node
        head_node = Node(data="head")
        linked_list = LinkedList(head_node=head_node)

        # Prepend new node
        new_node = Node(data="new_head")
        linked_list.prepend(new_node)

        # Check if the new node is prepended correctly
        self.assertEqual(linked_list.head_node.data, "new_head")
        self.assertEqual(linked_list.head_node.next_node.data, "head")

    def test_insert_at(self):
        # Create initial linked list with one node
        head_node = Node(data="head")
        linked_list = LinkedList(head_node=head_node)

        # Insert new nodes
        linked_list.append(Node(data="node1"))
        linked_list.append(Node(data="node2"))
        new_node = Node(data="inserted_node")
        linked_list.insert_node_by_index(1, new_node)

        # Check if the new node is inserted correctly
        self.assertEqual(linked_list.head_node.next_node.data, "inserted_node")

    def test_delete_at(self):
        # Create initial linked list with one node
        head_node = Node(data="head")
        linked_list = LinkedList(head_node=head_node)

        # Append new nodes
        linked_list.append(Node(data="node1"))
        linked_list.append(Node(data="node2"))

        # Delete node at index 1
        linked_list.delete_node_by_index(1)

        # Check if the node is deleted correctly
        self.assertEqual(linked_list.head_node.next_node.data, "node2")

    def test_clear(self):
        # Create initial linked list with one node
        head_node = Node(data="head")
        linked_list = LinkedList(head_node=head_node)

        # Append new nodes
        linked_list.append(Node(data="node1"))
        linked_list.append(Node(data="node2"))

        # Clear the linked list
        linked_list.clear()

        # Check if the linked list is cleared
        self.assertIsNone(linked_list.head_node, None)

    def test_get_node_by_index(self):
        # Create initial linked list with one node
        head_node = Node(data="head")
        linked_list = LinkedList(head_node=head_node)

        # Append new nodes
        linked_list.append(Node(data="node1"))
        linked_list.append(Node(data="node2"))

        # Get node by index
        node = linked_list.get_node_by_index(1)

        # Check if the correct node is returned
        self.assertEqual(node.data, "node1")

    def test_get_index_by_data(self):
        # Create initial linked list with one node
        head_node = Node(data="head")
        linked_list = LinkedList(head_node=head_node)

        # Append new nodes
        linked_list.append(Node(data="node1"))
        linked_list.append(Node(data="node2"))

        # Get index by data
        index_1 = linked_list.get_index_by_searching("node1")

        # Check if the correct index is returned
        self.assertEqual(index_1, 1)
        # Check the not be existed keyword in the linked list
        index_2 = linked_list.get_index_by_searching("Not existed data")
        self.assertEqual(index_2, -1)


if __name__ == "__main__":
    unittest.main()
