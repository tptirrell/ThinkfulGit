import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import scipy.stats


loansData = pd.read_csv('loansData.csv')

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: round(float(x.strip('%'))/100,4))
loansData['Annual.Income'] = loansData['Monthly.Income'].map(lambda x: 12*x)
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(x[:3]))

annual_inc = loansData['Annual.Income']
annual_inc[np.isnan(annual_inc)] = 0
ficoscore = loansData['FICO.Score']
ficoscore[np.isnan(ficoscore)] = 0
int_rate = loansData['Interest.Rate']
int_rate[np.isnan(int_rate)] = 0
home_ownership = [4 if x == 'OWN' else 3 if x == 'MORTGAGE' else 2 if x == 'RENT' else 1 if x == 'OTHER' else 0 for x in loansData['Home.Ownership']]
loanamt = loansData['Amount.Requested']
loanamt[np.isnan(loanamt)] = 0


y = np.matrix(int_rate).transpose()
#x = np.matrix(annual_inc).transpose()

x1 = np.matrix(annual_inc).transpose()
x2 = np.matrix(home_ownership).transpose()
x3 = np.matrix(loanamt).transpose()
x4 = np.matrix(ficoscore).transpose()
x = np.column_stack([x1,x2,x3,x4])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

#print (f.summary())

print ('Coefficients: ', f.params[0:2])
print ('Intercept: ', f.params[2])
print ('P-Values: ', f.pvalues)
print ('R-Squared: ', f.rsquared)

#print (x if np.isnan(annual_inc) == True for x in annual_inc)
