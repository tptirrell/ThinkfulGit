from scipy import stats
import pandas as pd

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East_Midlands,4.89,3.34
West_Midlands,5.63,3.47
East_Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern_Ireland,4.02,4.56'''

data = data.split()
data = [i.split(',') for i in data]

column_names = data[0] 
data_rows = data[1::] 
df = pd.DataFrame(data_rows, columns=column_names)


for i in range(len(df['Alcohol'])):
	df['Alcohol'][i] = float(df['Alcohol'][i])
	df['Tobacco'][i] = float(df['Tobacco'][i])

alcoholmode = df['Alcohol'].mode()
tobaccomode = df['Tobacco'].mode()

print ("The mean spend of Alcohol and Tobacco is $%.2f and $%.2f, respectively." % (df['Alcohol'].mean(), df['Tobacco'].mean()))
print ("The median spend of Alcohol and Tobacco is $%.2f and $%.2f, respectively." % (df['Alcohol'].median(), df['Tobacco'].median()))
try:
	print ("The mode spend of Alcohol and Tobacco is $%.2f and $%.2f, respectively." % (alcoholmode,tobaccomode))
except:
	print("The mode does not exist for this dataset.")
print ("The std dev of spend of Alcohol and Tobacco is $%.2f and $%.2f, respectively." % (df['Alcohol'].std(), df['Tobacco'].std()))
print ("The range of spend of Alcohol and Tobacco is $%.2f and $%.2f, respectively." % (max(df['Alcohol']) - min(df['Alcohol']), max(df['Tobacco']) - min(df['Tobacco'])))
print ("The variance of spend of Alcohol and Tobacco is $%.2f and $%.2f, respectively." % (df['Alcohol'].var(), df['Tobacco'].var()))
