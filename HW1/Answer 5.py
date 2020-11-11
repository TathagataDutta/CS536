print(chr(27) + "[2J")		#clear terminal

import numpy as np

n = 100		#features
L = 10		#dist. between 0 to L
MAX_ITER = 1000

np.random.seed(0)		#keeping results same

#Generating the (pseudo) random data (uniform distribution)
data = []
for i in range(MAX_ITER):
    data.append(np.random.uniform(0, L, n))

estd_l_mom = []			#estimated L M.O.M. vector
estd_l_mle = []			#estimated L M.L.E. vector

# Calculating estimated M.O.M. and M.L.E.
for i in range(len(data)):
    estd_l_mom.append(2*np.mean(data[i]))
    estd_l_mle.append(max(data[i]))

# Calculating estimated MSEs
estd_mse_mom = 0
for val in estd_l_mom:
	estd_mse_mom += pow((val - L),2)
estd_mse_mom = estd_mse_mom/MAX_ITER

estd_mse_mle = 0
for val in estd_l_mle:
	estd_mse_mle += pow((val - L),2)
estd_mse_mle = estd_mse_mle/MAX_ITER

print("Estimated MSE MOM: ",estd_mse_mom)
print("Estimated MSE MLE: ",estd_mse_mle)

# Calculating theoretical MSEs
theoretical_mse_mom = pow(L,2)/(3*n)
theoretical_mse_mle = (2*pow(L,2))/((n+2)*(n+1))

print("Theoretical MSE MOM: ",theoretical_mse_mom)
print("Theoretical MSE MLE: ",theoretical_mse_mle)

# Difference between estimated and theoretical MSEs
print("Absolute difference between theoretical and estimated MSE w.r.t. MOM: ",abs(theoretical_mse_mom - estd_mse_mom))
print("Absolute difference between theoretical and estimated MSE w.r.t. MLE: ",abs(theoretical_mse_mle - estd_mse_mle))