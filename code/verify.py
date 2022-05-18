import numpy as np 
from numpy import random as rn

a = b = rn.randint(0,2) 

Pr_A_Bcom_B_Acomp = a*(1-b) + b*(1-a)

print('Pr(A(B_comp) + B(A_comp))=',(Pr_A_Bcom_B_Acomp))
