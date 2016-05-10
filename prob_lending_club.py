import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

#reads data from csv
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')


#cleans data - removing rows with null values
loansData.dropna(inplace=True)

#loads data into pandas dataframe (***loansdata has no attribute .split() )
loansData = loansData.split()
loansData = [i.split(',') for i in loansData]
column_names = loansData[0] 
data_rows = loansData[1::] 
df = pd.DataFrame(data_rows, columns=column_names)



#creates and saves boxplot
loansData.boxplot(column='Amount.Requested')
plt.savefig("boxplot.png")
plt.show()

loansData.hist(column='Amount.Requested',histtype='bar')
plt.show()


plt.figure('QQ Plot')
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()
