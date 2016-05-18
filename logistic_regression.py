import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import scipy.stats
import math

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')


loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: round(float(x.strip('%'))/100,4))
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x.strip(' months'))
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(x[:3]))


intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()


loansData.to_csv('loansData_clean.csv', header=True, index=False)


interest = loansData['Interest.Rate']
interest = [0 if x < .12 else 1 for x in interest]
loansData['IR_TF'] = interest

loansData['Intercept'] = 1.0

ind_vars = ['FICO.Score','Amount.Requested','Intercept']

logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])
result = logit.fit()
coeff = result.params


def logistic_function(a,b):
	p = 1/(1 + math.exp((coeff['Intercept'] + coeff['FICO.Score']*a - coeff['Amount.Requested']*b)))
	return p


p = logistic_function(720,10000)
print (p)
