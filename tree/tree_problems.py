# Problem 1: Create BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_bst(arr):
    start_index = 0
    end_index = len(arr)-1
    mid_index = end_index//2

    root = Node(arr[mid_index])
    attach_child(arr, root, start_index, mid_index-1, True)
    attach_child(arr, root, mid_index+1, end_index, False)
    t=1
    print("--- BST Creation Done ---")


def attach_child(arr, parent, start, end, is_left):

    offset = (end-start)//2
    mid_index = start+offset
    if offset < 0 or mid_index >= len(arr):
        return

    if is_left:
        parent.left = Node(arr[mid_index])
        parent = parent.left

    else:
        parent.right = Node(arr[mid_index])
        parent = parent.right
    attach_child(arr, parent, start, mid_index - 1, True)
    attach_child(arr, parent, mid_index+1, end, False)


create_bst([2, 3, 4, 5, 6, 7])
