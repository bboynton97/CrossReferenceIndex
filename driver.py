from tree import BST
from tree import Node

print("Please enter the relative route to the text file you would like to analyze.")
path = raw_input("> ")

tree = BST()

with open(path, "r") as input_file: #open file
  for i, line in enumerate(input_file): # loop through every line
    line = line.replace('.','') #make every word delimator a space
    line = line.replace(',','')
    line = line.replace('?','')
    line = line.replace('\n','')

    if line[0] != "#":
        words = line.split(" ") #split on spaces
        for word in words:
            word = word[:10]
            print("-------\ninserting {}".format(word))
            tree.insert({"word":word,"lines":[i+1]})

tree.display()
