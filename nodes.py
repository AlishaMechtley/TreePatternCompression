from __future__ import division
'''
Created on Jan 15, 2012

@author: Alisha Rossi
'''
# Alisha Rossi

import random



class Node:
	def __init__(self, Name = None): # constructor
		#instance variables
		self.parent = None      # Each parent has no parent (root), and defines the cluster
		self.position = None    # [x, y, z]    
		self.children = []      # Each parent has a list of children
								#Just take length of list of children
		
	#setters    
	def reParent(self, parent):
		self.parent = parent
		parent.addChild(self)
	def setPosition(self,position):
		self.position = position
	def addChild(self, child):
		self.children += [child]

# functions
def sqDistance(node_i,newNode):
	#d=(node_i.position[0]-newNode.position[0])**2 + (node_i.position[1]-newNode.position[1])**2 + (node_i.position[2]-newNode.position[2])**2
	sqx= min((node_i.position[0]-newNode.position[0])**2,(node_i.position[0]-newNode.position[0]-1)**2,(node_i.position[0]-newNode.position[0]+1)**2)
	sqy=min((node_i.position[1]-newNode.position[1])**2,(node_i.position[1]-newNode.position[1]-1)**2,(node_i.position[1]-newNode.position[1]+1)**2)
	sqz=min((node_i.position[2]-newNode.position[2])**2, (node_i.position[2]-newNode.position[2]-1)**2, (node_i.position[2]-newNode.position[2]+1)**2)
	return sqx+sqy+sqz
	
	
def reCluster(oldParent, newParent):                                        # reAssign the children of a parent to a new parent
	for child in oldParent.children:                                    # assign all children to the new parent
			child.reParent(newParent)
	oldParent.reParent(newParent)                                      # old parent becomes child of new parent
	oldParent.children = []                                             # old parent is now a child and has no children      

averageN = 0

#for i in range(100):
f = open('sphereFreq.txt', 'w')
f.write('#Number of spheres (N), Number of clusters, Largest cluster size\n')


for i in range(1000):
	nodeList=[]                                                             # all nodes
	numClusters=0                                                           # keep track of the total number of clusters
	
	
	for j in range(10001):
                                                         # greatest number of children for all neighbors and parents of neighbors, technically cluster size minus two (the parent and myNode) 
		parentSizes=[]
		neighborList=[]                                                      # temporary list of neighbors for a new node
		myNode=Node()
		myNode.setPosition((random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
		#print "I am " + str(myNode) + " my position is " + str(myNode.position)
		
		for node_i in nodeList:
			d=sqDistance(node_i,myNode)
			#if d < 0.4:                                                     	# Find neighbors
			if d < 0.0004:
				neighborList+=[node_i]                                          # and add them to a list
			if node_i.parent is None:											# It's a root 
				parentSizes+=[len(node_i.children)+1]
		
		if len(nodeList)>0:
			assert len(nodeList)==sum(parentSizes)
			f.write('%i %i %i\n' % (len(nodeList),len(parentSizes), max(parentSizes)))
			numClusters=len(parentSizes)
		#print "Number of clusters is " +  str(numClusters)
		
		if len(neighborList)==1:                                                # if there's only one neighbor
			if neighborList[0].parent is not None:                              # and it has a parent
				myNode.reParent(neighborList[0].parent)                        # then the neighbor's parent becomes myNode's parent
				#print "My parent is my neighbor " +str(neighborList[0]) + "'s parent: " + str(myNode.parent)
			else:                                                               # or if the neighbor has no parent, it is a root and
				myNode.reParent(neighborList[0])                               # that gets a(nother) child
				#print "My neighbor: " + str(myNode.parent)  + " is now my parent"
												 
		elif len(neighborList)>1:                                               # if more than one neighbor exists
			for neighbor in neighborList:                                       # for each neighbor
				#print "neighbor is " + str(neighbor)
				try: 
					if neighbor.parent is not None:                             # NEIGHBOR HAS A PARENT
						#print "neighbor.parent is " + str(neighbor.parent)
						if myNode.parent is not None:							# MY NODE HAS A PARENT
							if myNode.parent != neighbor.parent:				# NEIGHBORS PARENT IS NOT ALREADY MY PARENT
								if len(neighbor.parent.children)>len(myNode.parent.children):     # NEIGHBOR'S PARENT HAS MORE CHILDREN THAN MINE
									#neighborParentSet.remove(myNode.parent)
									reCluster(myNode.parent, neighbor.parent)
									myNode.parent=neighbor.parent
									#neighborParentSet.add(neighbor.parent)
									#numClusters=numClusters-1
									#print "myNode's parent set to neighbor's parent:" +  neighbor.parent
								else: 
									#print "NEIGHBORS PARENT DOES NOT HAVE MORE CHILDREN THAN MY PARENT"
									reCluster(neighbor.parent, myNode.parent)
									#numClusters=numClusters-1
							#else: #print "NEIGHBOR'S PARENT IS ALREADY MY PARENT"
						else: 
							#print "MY NODE HAS NO PARENT"
							myNode.parent=neighbor.parent
					else: 
						#print "NEIGHBOR HAS NO PARENT"
						if myNode.parent is not None:							# MY NODE HAS A PARENT
							if myNode.parent != neighbor:						# NEIGHBOR IS NOT MY NODE'S PARENT
								if len(neighbor.children)>len(myNode.parent.children):     # NEIGHBOR HAS MORE CHILDREN THAN MY NODE'S PARENT
									#neighborParentSet.remove(myNode.parent)
									reCluster(myNode.parent, neighbor)
									#neighborParentSet.add(neighbor)
									myNode.parent=neighbor
									#numClusters=numClusters-1
									#print "myNode's parent was set to" +  neighbor
								else: 
									reCluster(neighbor, myNode.parent)
							#else: #print "MY NODE'S PARENT IS ALREADY MY NEIGHBOR"    
						else: 
							myNode.parent=neighbor				
				except:                                     
					print "exception occured"
			myNode.parent.addChild(myNode)                  #what if two neighbors with no children?
		nodeList+=[myNode] #add current node to the list
	#print "N is: " + str(len(nodeList))
	#averageN+=len(nodeList)/100							#division from the future!
f.close()

#print "Final average N is " + str(averageN)
