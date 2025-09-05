"""
Print only left view of the Binary tree

   1
   
2     3

output: 1, 2

     1
     
   2     3

4    5 6     7
                8
                
output: 1,2, 4, 8
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class LeftView:
    def __init__(self):
        self.root = None
        self.max_level = 0

    def leftView(self, root, level, result):
        if root is None:
            return result

        if self.max_level < level:
            self.max_level = level
            result.append(root.value)

        self.leftView(root.left, level + 1, result)
        self.leftView(root.right, level + 1, result)

        return result

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class LeftView1:
    def __init__(self):
        self.root = None
        self.max_level = 0

    def left_view(self, root, level):
        if root is None:
            return
        if self.max_level < level:
            print(f"{root.value}", end=" ")
            self.max_level = level

        self.left_view(root.left, level + 1)
        self.left_view(root.right, level + 1)


node = Node(1)
node.left = Node(10)
node.right = Node(20)
node.right.right = Node(40)
lv = LeftView()

print(lv.leftView(node, 1, []))

            