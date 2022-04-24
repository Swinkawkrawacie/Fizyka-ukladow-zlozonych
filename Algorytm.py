#!/usr/bin/env python 

import numpy as np
from numba import njit
import random

@njit
def alg_met(L,T,K):
    b = np.arange(-1,L+1)
    b[0] = L-1
    b[L+1] = 0
    N=L**2
    S = np.ones((L,L))
    #S = np.random.choice([-1,1],(L,L))
    #S_data = [np.copy(S)]
    m_data = [S.mean()]
    K_count = 0
    while K_count<K:
        K_count += 1
        op_count=0
        while op_count<N:
            op_count += 1
            i = np.random.randint(L)
            j = np.random.randint(L)
            dE=2*S[i][j]*(S[b[i]][j] + S[b[i+2]][j] + S[i][b[j]] + S[i][b[j+2]])
            if dE<=0:
                S[i][j] *= -1
            else:
                x = random.random()
                if x<np.exp(-dE/T):
                    S[i][j] *= -1
        m_data.append(S.mean())
        #S_data.append(np.copy(S))
    #return S_data
    return m_data

    
if __name__ == "__main__":
    #s1_1 = alg_met(10,1,10**6)
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\'+"L10_T1",s1_1, allow_pickle=True)
    #s1_2 = alg_met(10,2.26,10**6)
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\'+"L10_T2",s1_2, allow_pickle=True)
    #s1_3 = alg_met(10,4,10**6)
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\'+"L10_T3",s1_3, allow_pickle=True)
    #s2_1 = alg_met(100,1,10**4)
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\'+"L100_T1",s2_1, allow_pickle=True)
    #s2_2 = alg_met(100,2.26,10**4)
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\'+"L100_T2",s2_2, allow_pickle=True)
    #s2_3 = alg_met(100,4,10**5)
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\'+"L100_T3",s2_3, allow_pickle=True)
    #m10 = alg_met(10,1.7,10**6)
    #np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\danem\\m10.txt',m10)
    #m50 = alg_met(10,1.7,10**6)
    #np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\danem\\m50.txt',m50)
    #m100 = alg_met(10,1.7,10**6)
    #np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\danem\\m100.txt',m100)
    m=[]
    for i in np.arange(1,3.5,0.2):
        m.append(alg_met(10,i,10**6))
    np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\danem\\'+"m_zakres",m, allow_pickle=True)


    # alg_met(10,1,10**6,"L10_T1_2_")