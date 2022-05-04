#!/usr/bin/env python 

import numpy as np
from numba import njit
import random

@njit
def is_mcs(S,T,L,N,b):
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
    return S.mean(), np.copy(S)



def alg_met(L,T,K,M=True, matr = True, ran = False):
    b = np.arange(-1,L+1)
    b[0] = L-1
    b[L+1] = 0
    N=L**2
    S = np.ones((L,L))
    if ran:
        for i in range(L):
            for j in range(L):
                if random.random()<0.5:
                    S[i][j] = -1
    if matr:
        S_data = [np.copy(S)]
    if M:
        m_data = [S.mean()]
    K_count = 0
    while K_count<K:
        K_count += 1
        m,S = is_mcs(S,T,L,N,b)
        if matr:
            S_data.append(np.copy(S))
        if M:
            m_data.append(m)
    if matr:
        if M:
            return m_data, S_data
        else:
            return S_data
    elif M:
        return m_data
    return


def gen_txt(T,K,L=10,M=True, matr=True, k0=0,r=False, name=''):
    if M==False:
        if matr:
            if L==10:
                s = alg_met(10,T,K,False,ran=r)
                for i in [0,100,1000,4000,8000]:
                    np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\L10_T'+str(T)+'_'+str(i)+name+'.txt',s[i])
            else:
                s = alg_met(L,T,K,False,ran=r)
                for i in [0,1000,4000,7000,10000]:
                    np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\L'+str(L)+'_T'+str(T)+'_'+str(i)+name+'txt',s[i])
    else:
        if isinstance(T,int) or isinstance(T,float):
            if matr:
                if L==10:
                    new_m, new_s = alg_met(L,T,K,ran=r)
                    for i in [0,100,1000,4000,8000]:
                        np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\L10_T'+str(T)+'_'+str(i)+name+'.txt',new_s[i])
                else:
                    new_m, new_s = alg_met(L,T,K,ran=r)
                    for i in [0,1000,4000,7000,10000]:
                        np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\L'+str(L)+'_T'+str(T)+'_'+str(i)+name+'.txt',new_s[i])
                np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane1\\m'+str(L)+'_T'+str(T)+name+'.txt',new_m)
            else:
                new_m = alg_met(L,T,K,matr=False,ran=r)
                np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\m'+str(L)+'_T'+str(T)+name+'.txt',new_m)
        else:
            new_m = []
            for i in T:
                new_m.append(alg_met(L,i,K, matr=False,ran=r))
            average_m=[]
            for i in new_m:
                average_m.append(sum(abs(k) for k in i[k0:])/len(i[k0:]))
            np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\m'+str(L)+name+'.txt',average_m)

    
if __name__ == "__main__":
    #gen_txt(2.26,10**6)
    #gen_txt(1.7,10**6)
    #for i in range(1,10):
    #    gen_txt(1.7,10**6,matr=False, name=str(i))
    for i in range(1,10):
        gen_txt(1.7,10**6,50,matr=False, name=str(i))