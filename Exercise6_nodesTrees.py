
"""
Exercise 6 - Creating and Using Node and Tree Classes
@author: jembrown
Below is the beginning of a Node class definition and a simple example of how
to link nodes to form a tree. Use this as a springboard to start thinking about:
- What other attributes of a Node might we like to store?
- How do we define a Tree class? What attributes should it have?
- Can you write a function to print out a parenthetical tree string 
   (e.g., ((spA,spB),spC)) if the only argument passed to the function is a
   root node? This will require recursion.
"""

# ---> Defining Node and Tree classes <---
from ContinuousMarkovChain import ctmc

class Node:
    
    def __init__(self,name="",parent=None,children=None):
        self.name = name
        self.parent = None
        if children is None:
            self.children = []
        else:
            self.children = children
        
        
        
# ---> Creating and linking nodes <---
 
# Creating nodes to build this simple three-taxon tree: ((spA,spB),spC)
       
#  spA     spB  spC
#    \    /     /
#     \  /     /
#      \/     /
#       \    /
#        \  /
#         \/
#         |

# Define the root node to start. It currently has no parents or children.
root = Node("root") 

# Define a node for species C. It is a direct descendant of the root.
spC = Node("SpeciesC",parent=root)
root.children.append(spC)   # Adds spC as a child of the root

# Define a node for the ancestor of species A and B, descending from the root.
ancAB = Node("ancAB",parent=root)
root.children.append(ancAB)
spA = Node("SpeciesA",parent=ancAB) # Creates spA with ancAB as its parent.
spB = Node("SpeciesB",parent=ancAB) # Creates spB with ancAB as its parent.
ancAB.children.append(spA)
ancAB.children.append(spB)


print("ancAB's children: ")
for child in ancAB.children:
    print child.name
    
print("")
print("root's children: ")
for child in root.children:
    print child.name

# Play around with nodes and see if you can build more complicated trees!


# Eventually, we will want to create a Tree class, where a parenthetical tree
# string is passed as an argument to the constructor and it automatically creates
# all the nodes and links them together. Start thinking about how to do that.


# Let's go ahead and define a Tree object that houses all these nodes and 
# organizes methods associated with them.


# We'll need this later, I promise. It's always better to put import statements
# outside of class definitions. In fact, it's best to put them all at the top
# of a file. This imports the ctmc class that we previously defined.

class Tree:
    """
    Defines a class of phylogenetic tree, consisting of linked Node objects.
    """
    
    def __init__(self):
        """
        The constructor really needs to be more flexible, but for now we're 
        going to define the whole tree structure by hand. This just uses
        the same statements we used above. By next Thurs (3/19), see if you can
        write a constructor that takes a parenthetical tree as its argument and 
        builds the corresponding tree in memory. 
        """
        self.root = Node("root") 
        self.spC = Node("SpeciesC",parent=self.root)
        self.root.children.append(self.spC)
        self.ancAB = Node("ancAB",parent=self.root)
        self.root.children.append(self.ancAB)
        self.spA = Node("SpeciesA",parent=self.ancAB)
        self.spB = Node("SpeciesB",parent=self.ancAB)
        self.ancAB.children.append(self.spA)
        self.ancAB.children.append(self.spB)
        # Now, let's add branch lengths to our Node objects (remember, these fields
        # can be added arbitrarily in Python). In the future, we should probably include
        # branch lengths in the Node constructor.
        self.spA.brl = 0.1
        self.spB.brl = 0.1
        self.spC.brl = 0.2
        self.ancAB.brl = 0.1
        self.root.brl = 0
        # We're also going to add lists to each node that will hold simulated
        # sequences.
        self.spA.seq = []
        self.spB.seq = []
        self.spC.seq = []
        self.ancAB.seq = []
        self.root.seq = []
        self.setModels(self.root)

    # Write a recursive function that takes the root node as its only argument and
    # prints out all the names of the terminal nodes in the tree. Due next Tues (3/17).
    
    def printNodes(self, node):
        if node.children == []: # No children = terminal node
			print (node.name) 
        else: # If there are children, continue down the branch until you reach terminal node(s)
		for child in node.children:
			self.printNames(child) 
    """
        A method of a Tree object that will print out the names of its
        terminal nodes.
    """
    # Write a recursive function to calculate the total tree length (the sum of
    # all the branch lengths). Again, the root node of a tree should be the only 
    # argument the first time this function is called. Due next Tues (3/17).
    
    def treeLength(self,node):
        # Method to calculate and return total tree length.
        totaLength = 0 # Set initial branch length to zero. Define outside of loop
        if node.children == []: # Check to see if current node is a terminal node
            #Terminal branch returns branch length
            totaLength += node.brl # If terminal node, increase total length by node.brl
            return totaLength
        else: # If current node is not a terminal node
		totaLength += node.brl # Increase total length by node.brl
		for child in node.children:
			totaLength += self.treeLength(child) # Increase total length by branch length of children
		return totaLength

    # Write a recursive function that takes the root node as one of its arguments
    # and prints out a parenthetical (Newick) tree string. Due next Tues (3/17).
    
    def newick(self,node):
        # Print Tree as a parenthetical string (Newickk format): 
        Tree_String = "(" # Beginning of parenthetical string (Newick format)
        
        if node.children != []: # If the node is not a terminal node
            Tree_String += node.name + ":" + str(node.brl) # Add ":" and branch length to string
            for child in node.children: 
                if node.children[-1] == child: #If the parent is not the root
                    Tree_String += self.newick(child) # Calls newick again
                else:
                    Tree_String += self.newick(child) + "," # adds "," to string then calls newick again
            Tree_String += ")" 
            return Tree_String #Returns parenthetical string
            
        else: #  If terminal node
            Term_string = node.name + ":" + str(node.brl) # Return node.name ":" and branchlength
            return Term_string 

    # Now, let's write a recursive function to simulate sequence evolution along a
    # tree. This amounts to simply simulating evolution along each branch 
    # from the root towards the tips. We'll need to use our ctmc class for setting the 
    # conditions of our simulation, which is why we imported it above our tree 
    # class definition. In this case, we've stored the definition of our ctmc 
    # class in a separate file (ctmc.py) to keep our tree code compact.
    # Now, let's add a ctmc object to each internal node in our tree (except the
    # root). Again, it would be best to add the ctmcs as part of the Node
    # constructor, if we know that we'll be simulating data.
    
    # Try to get this simulator and associated functions working by next Thurs. (3/19)    
    
    def setModels(self,node):
        """
        This method of a Tree object defines a ctmc object associated with all
        nodes that have a branch length (i.e., all but the root).
        """
        # Prints out terminal nodes
        for i in node.children:							
			self.printNodes(i)

    def simulate(self,node):
        """
        This method simulates evolution along the branches of a tree, taking
        the root node as its initial argument.
        """
        if node.children == []: # If terminal node
            node.seq = ctmc().simulator() # Simulate seq evol (current node)
            
        else:
            node.seq = ctmc().simulator() # Simulate seq evol (current node)
            for child in node.children: 
                self.simulate(child) # Run simulator for each child
        
    def printSeqs(self,node):
        """
        This method prints out the names of the tips and their associated
        sequences as an alignment (matrix).
        """
        self.matrix=[] # Create empty list to append tip names and tip seqs
        if node.children == []: #If terminal node
            self.matrix.append(node.name) # Append name
            self.matrix.append(node.seq) # Append seq
            
        else: # If != terminal node 
            for child in node.children: #run printSeqs for each child
                self.printSeqs(child)

        return self.Matrix 
