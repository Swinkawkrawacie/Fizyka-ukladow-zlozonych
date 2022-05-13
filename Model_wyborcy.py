#!/usr/bin/env python 

import numpy as np
from numba import njit
import random

@njit
def mw_mcs(S, N, b):
    op_count=0
    while op_count<N:
        op_count += 1
        i = np.random.randint(N)
        x = random.random()
        if x<1/2:
            S[i] = S[b[i]]
        else:
            S[i] = S[b[i+2]]
    return np.copy(S)

@njit
def alg_mw(N:int, x):
    Np = round(x*N)
    b = np.arange(-1,N+1)
    b[0] = N-1
    b[N+1] = 0
    S = np.ones(N)
    for i in range(100-Np):
        S[np.random.randint(N)] = -1
    base_sum = sum(S)
    wanted_sum = 2*Np-N
    while base_sum < wanted_sum:
        pos_ind = np.where(S == -1)[0]
        k = pos_ind[np.random.randint(len(pos_ind))]
        S[k] = 1
        base_sum = sum(S)
    while base_sum > wanted_sum:
        pos_ind = np.where(S == 1)[0]
        k = pos_ind[np.random.randint(len(pos_ind))]
        S[k] = -1
        base_sum = sum(S)
    
    op_count = 0
    while sum(S)!=-N and sum(S)!=N:
        S = mw_mcs(S, N, b)
        op_count += 1
    
    if sum(S) == N:
        return 1, op_count
    else:
        return 0, op_count

@njit
def gen_mw(N, L, delta_x):
    x = 0
    results = []
    while round(x,2) <= 1:
        time = 0
        prob = 0
        for i in range(L):
            p,t = alg_mw(N, x)
            prob += p
            time += t
        time /= L
        prob /= L
        results.append([x, prob, time])
        x += delta_x 
    return results

def gen_txt(N, L, delta_x):
    results = gen_mw(N, L, delta_x)
    with open('N'+str(N)+'dx'+str(delta_x)+'L'+str(L)+'.txt','a') as f:
        for i in results:
            f.write(str(i[0])+'  '+str(i[1])+'  '+str(i[2])+'\n')

if __name__ == "__main__":
    #N = 10**2, 10**3, 10**4
    gen_txt(10**3,10**3,0.02)