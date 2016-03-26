from pylab import *

fileData=loadtxt("sphereFreqStub2.txt")
fileData=dstack(split(fileData,1000))
fileData=mean(fileData, axis=2)	#take average over all trials

for n in [10,100,1000,10000]:
	#average cluster size=n
	plot(fileData[0:n,0], fileData[0:n,1]) #gives us the oth column for x
	xlabel("Number of Spheres (N)")
	ylabel("Number of Clusters")
	show()
	#average cluster size=n
	plot(fileData[0:n,0], fileData[0:n,2]) #gives us the oth column for x
	xlabel("Number of Spheres (N)")
	ylabel("Average size of biggest cluster")
	show()
	
#Will get first and second plot for ten, then first and second for 100, etc
