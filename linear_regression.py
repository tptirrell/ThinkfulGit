import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import scipy.stats

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

cleaninterestrate = loansData['Interest.Rate'].map(lambda x: round(float(x.strip('%'))/100,4))
cleanloanlength = loansData['Loan.Length'].map(lambda x: x.strip(' months'))
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(x[:3]))


intrate = cleaninterestrate
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print (f.summary())

