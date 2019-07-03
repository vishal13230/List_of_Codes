#Calculation of future value
def fv_f(pv,r,n):
    return pv*(1+r)**n

fv_f(1000,0.6,5)

#calculation of present value
def pv_f(fv,r,n):
    return fv/(1+r)**n

pv_f(10486,0.6,5)

#cashflow
import numpy as np
cashFlows = np.array([100,50,40,30])
for cash in cashFlows:
    print(cash)
    
#calculation of NPV
def npv_f(rate, cashflows):
    total = 0.0
    for i in range(0,len(cashflows)):
        total += cashflows[i] / (1 + rate)**i
    return total

r = 0.6
cf = [-100,-30,50,40]
npv_f(r,cf)
