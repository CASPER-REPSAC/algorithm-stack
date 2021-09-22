import sys


class Node:
    def __init__(self, data, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right

    def search(self, data):
        if self.data == data:
            return self

        if self.left:
            if self.left.search(data):
                return self.left.search(data)

        if self.right:
            if self.right.search(data):
                return self.right.search(data)

    def preorder_traversal(self):
        if self.data != '.':
            print(self.data, end='')

        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()

        if self.data != '.':
            print(self.data, end='')

        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()

        if self.right:
            self.right.postorder_traversal()

        if self.data != '.':
            print(self.data, end='')


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    root = None

    # 트리 생성
    for i in range(n):
        data = sys.stdin.readline().split()

        if root is None:
            root = Node(data[0])
            root.left = Node(data[1])
            root.right = Node(data[2])
        else:
            node = root.search(data[0])
            node.left = Node(data[1])
            node.right = Node(data[2])

    root.preorder_traversal()
    print()
    root.inorder_traversal()
    print()
    root.postorder_traversal()