import urllib2
import sys
import numpy as np

target_url=("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data=urllib2.urlopen(target_url)

xList=[]
labels=[]
for line in data:
	row=line.strip().split(",")
	xList.append(row)
nrow=len(xList)
ncol=len(xList[1])	
#sys.stdout.write("Number of Rows of Data = "+str(nrow)+'\n')
#sys.stdout.write("Number of Columns of Data = "+str(ncol)+'\n')


type=[0]*3
colCounts=[]

"""for col in range(ncol):
	for row in xList:
		try:
			a=float(row[col])
			if isinstance(a,float):
				type[0]+=1
		except ValueError:
			if len(row[col])>0:
				type[1]+=1
			else:
				type[2]+=2
	colCounts.append(type)
	type=[0]*3						

sys.stdout.write("Col#\tNumber\tStrings\tOther")

iCol=0
for types in colCounts:
	sys.stdout.write(str(iCol)+'\t\t'+str(types[0])+'\t\t'+str(types[1])+'\t\t'+str(types[2])+"\n")
	iCol+=1
"""

col=3
colData=[]
for row in xList:
	colData.append(float(row[col]))	
colArray=np.array(colData)
colMean=np.mean(colArray)	
colsd=np.std(colArray)

sys.stdout.write("Mean = \t"+str(colMean)+'\t\t'+"Standar Deviation = \t"+str(colsd)+"\n")
#calculate quantile boundaries
ntiles=4

percentBdry=[]
for i in range(ntiles+1):
	percentBdry.append(np.percentile(colArray,i*(100)/ntiles))
print "Boundaries for 4 Equal Percentiles"
print percentBdry

ntiles=10
percentBdry=[]
for i in range(ntiles+1):
	percentBdry.append(np.percentile(colArray,i*(100)/ntiles))
print "Boundaries for 10 Equal Percentiles"
print percentBdry

col=60
colData=[]
for row in xList:
	colData.append(row[col])
unique=set(colData)
print "Unique Label Values"
print unique

catDict=dict(zip(list(unique),range(len(unique))))

catCount=[0]*2
print catCount

for elt in colData:
	catCount[catDict[elt]]+=1
print "Counts for Each Value of Categorical Label"
print list(unique)
print catCount	