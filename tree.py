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
        self.outputFile = open("output.txt","w")

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val): #Organizes alphabetically
        if val["word"] < currentNode.val["word"]: #if the word comes before the root word
            if currentNode.leftChild: #and left child exists
                self.insertNode(currentNode.leftChild, val) #give that left child a node with the val recursively
            else: #if not
                currentNode.leftChild = Node(val) #create a left child and give it the val
        elif val["word"] > currentNode.val["word"]: #same thing but for right
            if currentNode.rightChild:
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)
        else: #if they're equal
            lines = currentNode.val["lines"]
            lines += val["lines"] #add the new line count to the lines value
            currentNode.val['lines'] = lines #set the new lines

    def display(self): #display tree
        self.display_nodes(self.root)
        self.outputFile.close()

    def display_nodes(self, root): #recursively display nodes inorder
        if root is None: #if the node doesn't exist, stop
            return

        if root.getLeft() is not None: #display left first
            self.display_nodes(root.getLeft())

        print("{}\t\t\t{}".format(root.get()["word"], root.get()["lines"])) #then the root
        self.outputFile.write("{}\t\t\t{}\n".format(root.get()["word"], root.get()["lines"]))

        if root.getRight() is not None: #then the right
            self.display_nodes(root.getRight())
