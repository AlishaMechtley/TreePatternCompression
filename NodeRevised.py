'''
Created on Jan 15, 2012

@author: Alisha Rossi
'''
# Alisha Rossi
######################### make sure all parents in parent set are root nodes (with remove)
######################### and all smaller clusters are added to larger ones
import random

class Node:
    def __init__(self, Name = None): # constructor
        #instance variables
        self.parent = None      # Each parent has no parent (root), and defines the cluster
        self.position = None    # [x, y, z]    
        self.children = []      # Each parent has a list of children
                                #Just take length of list of children
        
    #setters    
    def setParent(self, parent):
        self.parent = parent
        parent.addChild(self)
    def setPosition(self,position):
        self.position = position
    def addChild(self, child):
        self.children += [child]    
        #child.parent = self            #redundant?
   

    #other functions            Use reCluster instead
    #def removeChildren(self):           
    #    self.children = []

# functions
def sqDistance(node_i,newNode):
        d=(node_i.position[0]-newNode.position[0])**2 + (node_i.position[1]-newNode.position[1])**2 + (node_i.position[2]-newNode.position[2])**2
        return d
        #to do: change to periodic Euclidean dist.
        
def reCluster(oldParent, newParent):                                        # reAssign the children of a parent to a new parent
        for child in oldParent.children:                                    # assign all children to the new parent
                child.setParent(newParent)
        oldParent.setParent(newParent)                                      # old parent becomes child of new parent
        oldParent.children = []                                             # old parent is now a child and has no children      


nodeList=[]                                                                 # all nodes
neighborList=[]                                                             # temporary list of neighbors for a new node
neighborParentSet = set([])                                                 # set of all (unique) parents of the neighboring Nodes
#broodSize=0                                                                 # greatest number of children for all neighbors and parents of neighbors, technically cluster size minus two (the parent and myNode) 
numClusters=0                                                               # keep track of the total number of clusters

for i in range(5):
    myNode=Node()
    myNode.setPosition((random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
    print "I am " + str(myNode) + " my position is " + str(myNode.position)
    
    for node_i in nodeList:
        d=sqDistance(node_i,myNode)
        #if d < 0.0004:                                                     # Find neighbors
        if d < 0.4:
            neighborList+=[node_i]                                          # and add them to a list
    
    if len(neighborList)==1:                                                # if there's only one neighbor
        if neighborList[0].parent is not None:                              # and it has a parent
            myNode.setParent(neighborList[0].parent)                        # then the neighbor's parent becomes myNode's parent
        else:                                                               # or if the neighbor has no parent, it is a root and
            myNode.setParent(neighborList[0])                               # that gets a(nother) child

    elif len(neighborList)>1:                                               # if more than one neighbor exists
        for neighbor in neighborList:                                       # for each neighbor
            try: 
                if neighbor.parent is not None:                             # NEIGHBOR HAS A PARENT
                    if myNode.parent is not None:                            # MY NODE HAS A PARENT
                        if myNode.parent != neighbor.parent:                # NEIGHBORS PARENT IS NOT ALREADY MY PARENT
                            if len(neighbor.parent.children)>len(myNode.parent.children):     # NEIGHBOR'S PARENT HAS MORE CHILDREN THAN MINE
                                neighborParentSet.remove(myNode.parent)
                                reCluster(myNode.parent, neighbor.parent)
                                myNode.parent=neighbor.parent
                                neighborParentSet.add(neighbor.parent)
                                numClusters=numClusters-1
                            else: 
                                neighborParentSet.remove(neighbor.parent)
                                reCluster(neighbor.parent, myNode.parent)
                                numClusters=numClusters-1
                    else: 
                        print "MY NODE HAS NO PARENT"
                        myNode.parent=neighbor.parent
                else: 
                    print "NEIGHBOR HAS NO PARENT"
                    if myNode.parent is not None:                            # MY NODE HAS A PARENT
                        if myNode.parent != neighbor:                        # NEIGHBOR IS NOT MY NODE'S PARENT
                            if len(neighbor.children)>len(myNode.parent.children):     # NEIGHBOR HAS MORE CHILDREN THAN MY NODE'S PARENT
                                neighborParentSet.remove(myNode.parent)
                                reCluster(myNode.parent, neighbor)
                                neighborParentSet.add(neighbor)
                                myNode.parent=neighbor
                                numClusters=numClusters-1
                            else: 
                                neighborParentSet.remove(neighbor.parent)
                                reCluster(neighbor, myNode.parent)
                                myNode.parent=neighbor
                                numClusters=numClusters-1
                    else: #myNode.parent is None:
                        myNode.parent=neighbor
                          
             
                    print "The largest cluster is now " + str(len(myNode.parent.children)+1) + " or " + str(broodSize + 2) # add one to include the parent, and another for itself
                    myNode.parent.addChild(myNode)                  #what if two neighbors with no children?
                    try:
                        neighborParentSet.remove(myNode.parent)         #don't want to rest all these to the same cluster
                    except:
                        print "MY NODE'S PARENT WAS NOT IN THE PARENT SET"
                    for root in neighborParentSet:                  # for parents of all neighbors
                        reCluster(root, myNode.parent)
                
            except:                                     
                print "exception occured"
                
    else:                                                   # if myNode's parent is not reset
        numClusters+=1                                      # myNode is stays a parent                          

    #broodSize=0           
    neighborList=[]
    neighborParentSet=set([])
    nodeList+=[myNode]                                  #add current node to the list

print "Number of clusters is " +  str(numClusters)

#I am not really keeping track of the cluster size... maybe use k-d tree for this?