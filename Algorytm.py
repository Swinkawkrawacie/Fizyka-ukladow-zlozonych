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
    for i in range(L):
        for j in range(L):
            if random.random()<0.5:
                S[i][j] = -1
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

def gen_txt(T,n,m=True,L=10):
    if m==False:
        if L==10:
            s = alg_met(10,T,10**6)
            for i in [0,100,1000,4000,8000]:
                np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\L10_T'+str(T)+'_'+str(i)+'_'+'.txt',s[i])
        else:
            s = alg_met(L,T,10**4)
            for i in [0,1000,4000,7000,10000]:
                np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\L'+str(L)+'_T'+str(T)+'_'+str(i)+'_'+'.txt',s[i])
    else:
        if isinstance(T,int) or isinstance(T,float):
            new_m = alg_met(L,T,10**6)
            np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\m'+str(L)+'_T'+str(T)+'.txt',new_m)
        else:
            new_m = []
            for i in T:
                new_m.append(alg_met(L,i,10**6))
            average_m=[]
            for i in new_m:
                average_m.append(sum(abs(k) for k in i[10**4:])/len(i[10**4:]))
            np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\m'+str(L)+'.txt',average_m)

    
if __name__ == "__main__":
    #------------------------------------L=10, uporządkowane---------------------------------------------------------------------
    #s1_1 = alg_met(10,1,10**6)
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\'+"L10_T1_uno",s1_1, allow_pickle=True)
    #s1_2 = alg_met(10,2.26,10**6)
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\'+"L10_T2_uno",s1_2, allow_pickle=True)
    #s1_3 = alg_met(10,4,10**6)
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\'+"L10_T3_uno",s1_3, allow_pickle=True)
    #------------------------------------L=100, uporządkowane---------------------------------------------------------------------
    #s2_1 = alg_met(100,1,10**4)
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\'+"L100_T1_uno",s2_1, allow_pickle=True)
    #s2_2 = alg_met(100,2.26,10**4)
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\'+"L100_T2_uno",s2_2, allow_pickle=True)
    #s2_3 = alg_met(100,4,10**4)
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\'+"L100_T3_uno",s2_3, allow_pickle=True)
    #----------------------------------------m dla T=1.7-------------------------------------------------------------------------
    #m10_uno = alg_met(10,1.7,10**6)
    #np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\danem\\m10_uno.txt',m10_uno)
    #m50_uno = alg_met(50,1.7,10**6)
    #np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\danem\\m50_uno.txt',m50_uno)
    m100_uno = alg_met(100,1.7,10**6)
    np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\danem\\m100_uno.txt',m100_uno)
    #m=[]
    #t_range = np.arange(1,2,0.2)
    #t_range = np.append(t_range,np.arange(2,2.6,0.1))
    #t_range = np.append(t_range,np.arange(2.6,3.5,0.2))
    #for i in t_range:
    #    m.append(alg_met(100,i,10**6))
    #np.save(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\danem\\'+"m100_zakres",m, allow_pickle=True)
