from collections import deque
from uuid import uuid4

# Node of tree
from queue import Queue


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.__node_id = uuid4().hex

    def node_id(self):
        return self.__node_id


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        node = Node(data)
        if self.root is None:
            print()
            self.root = node
            return
        node_location = self.__find_node_to_add_child(data, self.root)
        if node_location.data < data:
            node_location.right = node
        else:
            node_location.left = node

    def __find_node_to_add_child(self, data, node: Node):
        if node.data < data:
            if node.right is not None:
                return self.__find_node_to_add_child(data, node.right)
            else:
                return node
        elif node.left is not None:
            return self.__find_node_to_add_child(data, node.left)
        else:
            return node

    def display(self):
        node_queue = deque()
        node_queue.append(self.root)
        node_queue.append(None)
        while len(node_queue) > 0:
            current_node = node_queue.popleft()
            if current_node is not None:
                print(current_node.data, end=' ')
                if current_node.left is not None:
                    node_queue.append(current_node.left)
                if current_node.right is not None:
                    node_queue.append(current_node.right)
            elif len(node_queue) > 0:
                print()
                node_queue.append(None)

    # first complete your version of tv
    def tv(self):
        node_queue = Queue()
        node_queue.put(self.root)
        node_queue.put(None)
        node_map = {self.root.node_id(): 0}
        height_map = {}
        while node_queue.qsize() > 0:
            current_node = node_queue.get()

            if current_node is not None:

                node_id = current_node.node_id()
                height = node_map.get(node_id)
                is_height_exists = height_map.get(height)

                if is_height_exists is not True:
                    print(current_node.data, end=' ')
                    height_map[height] = True

                if current_node.left is not None:
                    node_map[current_node.left.node_id()] = height - 1
                    node_queue.put(current_node.left)

                if current_node.right is not None:
                    node_map[current_node.right.node_id()] = height + 1
                    node_queue.put(current_node.right)

            elif node_queue.qsize() > 0:
                node_queue.put(None)
                print()


my_tree = Tree()
my_tree.add(10)
my_tree.add(4)
my_tree.add(89)
my_tree.add(34)
my_tree.add(8)
my_tree.add(1)
my_tree.display()
print('=============')
my_tree.tv()
