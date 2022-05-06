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


def gen_txt(T,K:int,L:int=10,M:bool=True, matr:bool=True, k0:int=0,r:bool=False, name:str='',av=True):
    """
    Generate text file of spin configuration and/or trajectory
    @param T: temperature or a list of temperatures
    @param K: (int) amount of MCS
    @param L: (int) size of a matrix (default=10)
    @param M: (bool) equals True if the trajectory should be saved to a file (default=True)
    @param matr: (bool) equals True if the matrixes should be saved to a file (default=True)
    @param k0: (int) index to start calculating average with
    @param r: (bool) equals True if the base matrix should be unordered (default=False)
    @param name: (str) addition to the basic name (default='')
    """
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
                np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\m'+str(L)+'_T'+str(T)+name+'.txt',new_m)
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
            if av:
                np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\m'+str(L)+name+'.txt',average_m)
            else:
                m_2=[]
                for i in new_m:
                    m_2.append(sum(k**2 for k in i[k0:])/len(i[k0:]))
                pod = []
                for i in range(len(m_2)):
                    pod.append((m_2[i]-(average_m[i])**2)*L**2/T[i])
                np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\dane\\m'+str(L)+name+'pod.txt',pod)

    
if __name__ == "__main__":
    #gen_txt(2.26,10**6)
    #gen_txt(1.7,10**6,100, name=6)
    #for i in range(1,10):
    #    gen_txt(1.7,10**6,matr=False, name=str(i))
    #for i in range(1,10):
    #    gen_txt(1.7,10**6,50,matr=False, name=str(i))
    #for i in range(1,6):
    #    gen_txt(1.7,10**6,100,matr=False, name=str(i))
    #gen_txt(1.7,10**6,100,matr=False,r=True,name='6')
    #for i in range(101):
     #   gen_txt(2.26,10**5,L=100,matr=False, r=True, name='prob'+str(i))
    for i in range(4):
        gen_txt(1.7,10**5,matr=False,name=str(i+6), r=True)