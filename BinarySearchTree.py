class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        start = self.root
        while True:
            if start.value > new_val:
                if not start.left:
                    start.left = Node(new_val)
                    break
                else:
                    start = start.left
            else:
                if not start.right:
                    start.right = Node(new_val)
                    break
                else:
                    start = start.right

    def search(self, find_val):
        start = self.root
        while start:
            if start.value > find_val:
                start = start.left
            elif start.value < find_val:
                start = start.right
            else:
                return True
        return False
