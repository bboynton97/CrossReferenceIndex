class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def getLeft(self):
        return self.leftChild

    def getRight(self):
        return self.rightChild

class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val): #Organizes alphabetically
        if val["word"] < currentNode.val["word"]:
            if currentNode.leftChild:
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif val["word"] > currentNode.val["word"]:
            if currentNode.rightChild:
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)
        else: #if they're equal
            lines = currentNode.val["lines"]
            lines += val["lines"]
            currentNode.val['lines'] = lines
            print("\nequal -> {}".format(currentNode.val))

    def find(self, val):
        return self.findNode(self.root, val)

    def display(self):
        self.display_nodes(self.root)

    def display_nodes(self, root):
        if root is None:
            return

        if root.getLeft() is not None:
            self.display_nodes(root.getLeft())

        print("{}\t\t\t{}".format(root.get()["word"], root.get()["lines"]))

        if root.getRight() is not None:
            self.display_nodes(root.getRight())
