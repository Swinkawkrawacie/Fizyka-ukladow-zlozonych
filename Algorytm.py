#!/usr/bin/env python 

import numpy as np
import math
import random

def alg_met(L,T,K, file_name):
    kb = 1 #stała boltzmana
    J = 1
    S = np.ones((L,L))
    N=L**2
    name_count=0
    for z in range(K):
        op_count=0
        name_count+=1
        while op_count<N:
            op_count += 1
            i = math.floor(random.random()*L)
            j = math.floor(random.random()*L)
            s_neighbours = []
            s_ij = [i-1,i+1,j-1,j+1] 
            if s_ij[0]>=0:
                s_neighbours.append(S[s_ij[0]][j])
            if s_ij[1]<L:
                s_neighbours.append(S[s_ij[1]][j])
            if s_ij[2]>=0:
                s_neighbours.append(S[i][s_ij[2]])
            if s_ij[3]<L:
                s_neighbours.append(S[i][s_ij[3]])
            s = S[i][j]
            dE=2*J*s*sum(s_neighbours)
            if dE<=0:
                S[i][j] = -s
            else:
                x = random.random()
                if x<math.exp(-dE/(kb*T)):
                    S[i][j] = -s
        np.savetxt(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\L10_T2\\'+file_name+str(name_count)+'.txt',S)
        with open(r'C:\\Users\\mazur\\OneDrive\\Dokumenty\\GitHub\\Fizyka-ukladow-zlozonych\\L10_T2\\'+file_name+'m.txt','a',encoding = 'utf-8') as file:
            file.write(str(1/N*sum(sum(S)))+'\n')

if __name__ == "__main__":
    #alg_met(10,1,10**6,"L10_T1_")
    alg_met(10,2.26,10**6,"L10_T2_")