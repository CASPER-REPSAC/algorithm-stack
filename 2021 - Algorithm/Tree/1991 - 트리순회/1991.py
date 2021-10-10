import sys
input = sys.stdin.readline


#전위 순회 : 뿌리 -> 왼쪽 자식 -> 오른쪽 자식
#중위 순회 : 왼쪽 자식 -> 뿌리 -> 오른쪽 자식
#후위 순회 : 왼쪽 자식 -> 오른쪽 자식 -> 뿌리

class Node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right

def preorder(root):
  print(root.data, end='')
  if root.left != '.':
    preorder(tree[root.left])
  if root.right != '.':
    preorder(tree[root.right])

def inorder(root):
  if root.left != '.':
    inorder(tree[root.left])
  print(root.data, end='')
  if root.right != '.':
    inorder(tree[root.right])

def postorder(root):
  if root.left != '.':
    postorder(tree[root.left])
  if root.right != '.':
    postorder(tree[root.right])
  print(root.data, end='')

if __name__=="__main__":
    n = int(input())
    tree = {}

    for i in range(n): # 클래스 생성
        root, left, right = map(str, input().split())
        tree[root] = root(data=root, left=left, right=right)

    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])