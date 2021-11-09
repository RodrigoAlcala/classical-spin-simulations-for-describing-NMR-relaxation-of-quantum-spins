import random
import numpy as np
import matplotlib as plt

np.set_printoptions(precision=3)

g = 25166.2
h = 6.582e-16
r0 = 2.72e-10

def randomSpinGenerator():
    S = np.zeros((3,3))
    a,b = -1,1
    for m in range(3):
        for n in range(3):
            val = (b-a)*np.random.rand() + a
            val = round(val,2)
            S[m,n] = val
    
    norm1 = 1/np.sqrt((abs(S[0][0])**2 + abs(S[1][0])**2 + abs(S[2][0])**2))
    norm2 = 1/np.sqrt((abs(S[0][1])**2 + abs(S[1][1])**2 + abs(S[2][1])**2))
    norm3 = 1/np.sqrt((abs(S[0][2])**2 + abs(S[1][2])**2 + abs(S[2][2])**2))

    norm1 = round(norm1,2)
    norm2 = round(norm2,2)
    norm3 = round(norm3,2)

    S[0,0] = S[0,0]*norm1
    S[1,0] = S[1,0]*norm1 
    S[2,0] = S[2,0]*norm1

    S[0,1] = S[0,1]*norm2
    S[1,1] = S[1,1]*norm2
    S[2,1] = S[2,1]*norm2

    S[0,2] = S[0,2]*norm3
    S[1,2] = S[1,2]*norm3
    S[2,2] = S[2,2]*norm3

    #print("Norma S1: " + str(norm1))
    #print("Norma S2: " + str(norm2))
    #print("Norma S3: " + str(norm3))

    for m in range(3):
        for n in range(3):
            S[m,n] = round(S[m,n],3)
    #print(S)
    return S

#randomSpinGenerator()


def couplingConstants():
    S = randomSpinGenerator()
    J = np.zeros((3,3))
    #k = ((-1/2)*((g**2)*(h**2)))/(r0**3)
    #k = round(k,1)
    k = 1
    for m in range(3):
        for n in range(3):
            J[m,n]= k-k*3*((S[0,m]*S[0,n]+S[1,m]*S[1,n]+S[2,m]*S[2,n])**2)
            J[m,n] = round(J[m,n],3)
    
    J[1, 0] = J[0, 0]
    J[2, 0] = -0.5*J[0, 0]
    
    J[1, 1] = J[0, 1]
    J[2, 1] = -0.5*J[0, 1]
    
    J[1, 2] = J[0, 2]
    J[2, 2] = -0.5*J[0, 2]
    
    print("\n Matriz de Spines: \n")
    print(S)
    print("\n Matriz de Constantes de Acoplamiento: \n")
    print(J)
    return J



def sDot1x3():
    S = randomSpinGenerator()
    J = couplingConstants()
    Hm =  np.zeros((3, 1))

    Hm[0, 0] = S[0, 0]*J[0, 0] + S[0, 1]*J[0, 1] + S[0, 2]*J[0, 2]  
    Hm[1, 0] = S[1, 0]*J[1, 0] + S[1, 1]*J[1, 1] + S[1, 2]*J[1, 2]
    Hm[2, 0] = S[2, 0]*J[2, 0] + S[2, 1]*J[2, 1] + S[2, 2]*J[2, 2]
    
    Hm = np.transpose(Hm)
    
    S0 = S[:, 0]
    S1 = S[:, 1]
    S2 = S[:, 2]

    SDOT1 = np.array(np.cross(S0, Hm))
    SDOT2 = np.array(np.cross(S1, Hm))
    SDOT3 = np.array(np.cross(S2, Hm))


    print("\n Matriz h_m: \n")
    print(np.transpose(Hm))
    print("\n Cambios de S_m: \n")
    print(np.transpose(SDOT1))
    print("\n")    
    print(np.transpose(SDOT2))
    print("\n")
    print(np.transpose(SDOT3))
    print("\n")

sDot1x3()
