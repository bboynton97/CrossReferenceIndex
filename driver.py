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
        for word in words:#\ #for every word
            word = word[:10] #only keep first ten letters
            tree.insert({"word":word,"lines":[i+1]}) #insert into tree

tree.display()
