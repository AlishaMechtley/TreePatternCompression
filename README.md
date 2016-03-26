



Background

This problem consders the process of depositing spheres (nodes) of radius R=0.01 in a cubic box of unit side length. It is assumed that the boundaries of the box are periodic.

Spheres are deposited randomly and sequentially (one after another). The center of the sphere is given by (Xc,Yc,Zc) where these three coordinates are drwn as a point from the uniform random number distribution U[0,1].

The objective is to create a stochasitc process (using averages), meaning we have to repeat the experiment several times (e.g. 1000) to answer questions about clusters (trees) as a fraction of the number of deposited spheres N such as:

1) the number of clusters
2) the size (number of spheres) of the largest cluster
3) the size distribution of the clusters
4) the percolation threshold

The method checks whether two spheres intersect using the distance between their centers (less that 2R). It involves keeping track of the clusters to which the spheres belong using a "find union" algorithm in which we "find" where they belong and if the Spheres belong to two different clusters, we merge the clusters they belong to ("union"). We repeat this until we have a large enough N.

The data structure involved is a tree, most "find union" methods involve a tree data structure to represent growing clusters. Each cluster is stored as a separate tree.The spheres (which belong to a paticular cluster) are considered the nodes of a tree.


Algorithm

1) Initially the nodes are trees in their own right. Each is it's own root node and contains a record of it's own size which is 1.

2) When a node-node connection is detected a "bond" is added between the two. Think of this as a tree branch.

3) Each branch added joins together the two nodes. We follow pointers from each of these nodes separately until we reach the root nodes of the clusters to which they belong. Root nodes are identified by the fact that they do not present poiters to any other nodes. Then we go back along the paths we followed through each tree and adjust all the pointers allong those paths directly to the root node of that tree.


 ![Figure1](https://raw.githubusercontent.com/AlishaMechtley/TreePatternCompression/master/images/Algorithm.png)


Figure 1: An example of the tree structure described, here representing two clusters. The shaded nodes are the root nodes and the arrows represent pointers. When a “bond” is added (dotted line in center) that joins nodes which belong to different clusters (i.e., whose pointers lead to different root nodes), the two clusters must be amalgamated by making one (left) a subtree of the other (right). This is achieved by adding a new pointer from the root of one tree to the root of the other.



These steps are repeated until we have a single large cluster. At each step during the run, the tree structures on the lattice correctly describe all of the clusters of joined sites, allowing us to evaluate observable quantities of interest. For example, if we are interested in the size of the largest cluster on the lattice as a function of N, we simply keep track of the largest cluster size we have seen during the course of the algorithm.


# Results

The data structure and algorithm have been implemented.  To run the code, type the following into the command line:

```$python nodes.py```

It is currently set to do 1000 runs, but this will take a really long time so to test you can use less runs. To print the graphs, be sure that the number in line 4 of the plotmaker.py (currently set to 1000) matches the number of runs you did because it resizes the array for averaging. Then, type into the command line:

```$python plotmaker.py```


I carried out the simulation by increasing N until there was a single large cluster.  I ran the program for 20 hours on my laptop and it did not converge. The last step printed out that there were 146813 spheres, 1485 clusters, and 143845 spheres within the largest cluster.  The number of clusters was slowly decreasing and when plotted against the total number of spheres, it appeared that the clusters should converge to 1 cluster at around 176,441 spheres.

 ![Figure2](https://raw.githubusercontent.com/AlishaMechtley/TreePatternCompression/master/images/Results.png)


Improvement Note: There is a formula for the periodic Euclidian distance which involves a modulus and is much less time consuming than using conditional (if) statements or taking the minimum of 3 distances between every two nodes (like I have done). Using any precompiled library would improve the computational cost.  

I generate plots of (i) the average number of clusters as a function of N and the average size of the largest cluster as a function of N for N = 10,100,1000, and 10000. I then computed averages from 1000 different experiments at a given N.

Here are the plots for the average number of clusters as a function of the number of spheres (N) for N = 10; 100; 1000, and 10000.  The plot appears linear for N=10 and begins to curve downward as N increases.

 ![Figure2](https://raw.githubusercontent.com/AlishaMechtley/TreePatternCompression/master/images/ClustersVsSpheres10.png)
 
Figure 3: Number of clusters as a function of N for N = 10

 ![Figure3](https://raw.githubusercontent.com/AlishaMechtley/TreePatternCompression/master/images/ClustersVsSpheres100.png)
Figure 4: Number of clusters as a function of N for N = 100

 ![Figure4](https://raw.githubusercontent.com/AlishaMechtley/TreePatternCompression/master/images/ClustersVsSpheres1000.png)

Figure 5: Number of clusters as a function of N for N = 1000.

 ![Figure5](https://raw.githubusercontent.com/AlishaMechtley/TreePatternCompression/master/images/ClustersVsSpheres10000.png)

Figure 6: Number of clusters as a function of N for N = 10000

Here are the plots for the average size of the largest cluster as a function of N. For N = 10; 100; 1000, and 10000.  I computed the averages for 175 of the 1000 different experiments  at a given N.

  ![Figure6](https://raw.githubusercontent.com/AlishaMechtley/TreePatternCompression/master/images/ClusterSizeVsSpheres10.png)

Figure 7: Average size of the largest cluster as a function of N for N = 10
 
  ![Figure7](https://raw.githubusercontent.com/AlishaMechtley/TreePatternCompression/master/images/ClusterSizeVsSpheres100.png)

Figure 8: Average size of the largest cluster as a function of N for N = 100

 ![Figure8](https://raw.githubusercontent.com/AlishaMechtley/TreePatternCompression/master/images/ClusterSizeVsSpheres1000.png)

Figure 9:  Average size of the largest cluster as a function of N for N = 1000
 
  ![Figure9](https://raw.githubusercontent.com/AlishaMechtley/TreePatternCompression/master/images/ClusterSizeVsSpheres1000.png)

Figure 10: Average size of the largest cluster as a function of N for N = 10000
