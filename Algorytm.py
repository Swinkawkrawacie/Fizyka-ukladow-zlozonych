#!/usr/bin/env python 

import numpy as np
import math
import random

def alg_met(L,T,K, file_name):
    b = [i for i in range(-1,L+1)]
    b[0] = L-1
    b[L+1] = 0
    kb = 1 #stała boltzmana
    J = 1
    N=L**2
    #S = np.ones((L,L))
    S = np.random.choice([-1,1],(L,L))
    m_data = [1/N*sum(sum(S))]
    #name_count=0
    for z in range(K):
        op_count=0
        #name_count+=1
        while op_count<N:
            op_count += 1
            i = math.floor(random.random()*L)
            j = math.floor(random.random()*L)
            dE=2*J*S[i][j]*(S[b[i]][j] + S[b[i+2]][j] + S[i][b[j]] + S[i][b[j+2]])
            if dE<=0:
                S[i][j] *= -1
            else:
                x = random.random()
                if x<math.exp(-dE/(kb*T)):
                    S[i][j] *= -1
        m_data.append(1/N*sum(sum(S)))
        #np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\L10_T1_2\\'+file_name+str(name_count)+'.txt',S)
        #with open(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\danem\\'+file_name+'m.txt','a',encoding = 'utf-8') as file:
         #   file.write(str()+'\n')
    np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\danem\\'+file_name+'m.txt',m_data)

if __name__ == "__main__":
    #alg_met(10,1,10**6,"L10_T1_")
    #alg_met(10,2.26,10**6,"L10_T2_")
    #alg_met(10,4,10**6,"L10_T3_")
    alg_met(10,1.7,10**6,"uno_1_7_10")
    #alg_met(10,1.7,10**6,"1_7_10")
    #alg_met(10,1.7,10**6,"1_7_10_3")
    #alg_met(50,1.7,10**6,"1_7_50")


    # alg_met(10,1,10**6,"L10_T1_2_")