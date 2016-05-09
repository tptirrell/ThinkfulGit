import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import scipy.stats as stats
import collections

testlist = [1, 4, 5, 6, 9, 9, 9, 7, 12, 15, 8, 8, 11, 11, 11]

c = collections.Counter(testlist)

print(c)

# calculate the number of instances in the list
count_sum = sum(c.values())

for k in c:
	print("The frequency of number %s is %.2f" %(str(k),(float(c[k]) / count_sum)))

#creates and saves boxplot
plt.figure("Box Plot of Testlist")
plt.boxplot(testlist)
plt.savefig("boxplot.png")

#creates histogram
plt.figure("Histogram of Testlist")
plt.hist(testlist, histtype='bar')

#creates qq plot
plt.figure("QQ Plot of Testlist") 
graph1 = stats.probplot(testlist, dist="norm", plot=plt)
plt.show() 




