import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy.lib.function_base import kaiser
from scipy import interpolate
np.set_printoptions(precision=3)
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

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
            #J[m,n]= k-k*3*((S[0,m]*S[0,n]+S[1,m]*S[1,n]+S[2,m]*S[2,n])**2)
            J[m,n] = k-k*3*(1)
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
    return J,S


def sDot1x3():
    J,S= couplingConstants()
    Hm =  np.zeros((3, 1))
    Hm[0, 0] = S[0, 0]*J[0, 0] + S[0, 1]*J[0, 1] + S[0, 2]*J[0, 2]  
    Hm[1, 0] = S[1, 0]*J[1, 0] + S[1, 1]*J[1, 1] + S[1, 2]*J[1, 2]
    Hm[2, 0] = S[2, 0]*J[2, 0] + S[2, 1]*J[2, 1] + S[2, 2]*J[2, 2]
    #Hm[0, 0] = S[0, 1]*J[0, 1] + S[0, 2]*J[0, 2]
    #Hm[1, 0] = S[1, 1]*J[1, 1] + S[1, 2]*J[1, 2]
    #Hm[2, 0] = S[2, 1]*J[2, 1] + S[2, 2]*J[2, 2]
    Hm = np.transpose(Hm)    
    S0 = S[:, 0]
    S1 = S[:, 1]
    S2 = S[:, 2]
    SDOT1 = np.array(np.cross(S0, Hm))
    SDOT2 = np.array(np.cross(S1, Hm))
    SDOT3 = np.array(np.cross(S2, Hm))
    Sd = np.vstack((SDOT1,SDOT2,SDOT3)).T
    #print("\n Matriz h_m: \n")
    #print(np.transpose(Hm))
    print("\n Condiciones iniciales: \n")
    print(Sd)
    return Sd

sDot1x3()


def odes(S, t):
    ## ctes:
    J1 = -2
    J2 = -2
    J3 = 1
    #Asignamos cada ode a un elemento vector:
    S1,S2,S3,S4,S5,S6 = S[0],S[1],S[2],S[3],S[4],S[5]
    #definimos odes
    dS1 = S2*S6 + 2*S3*S5
    dS2 = -2*S3*S4 - S1*S6
    dS3 = -2*S1*S5 + 2*S2*S4

    dS4 = S5*S3 - 2*S6*S2
    dS5 = -2*S6*S1 - S4*S3
    dS6 = -2*S4*S2 + 2*S5*S1
    return [dS1,dS2,dS3,dS4,dS5,dS6]


def solver():
    c0 = [-0.375,-0.013,-0.925,0.411,0.758,0.498]
    #c0 = [1,-1,-1,1,1,-1]
    ## test ##
    #print(odes(x=c0,t=0))

    #declare a time vector

    t = np.linspace(0,200,100)

    S = solve_ivp(odes, c0, t)

    S1 = S[:, 0]
    S2 = S[:, 1]
    S3 = S[:, 2]
    S4 = S[:, 3]
    S5 = S[:, 4]
    S6 = S[:, 5]

    #plot

    plt.semilogy(t, S1)
    # plt.scatter(t, S2)
    # plt.scatter(t, S3)
    # plt.scatter(t, S4)
    # plt.scatter(t, S5)
    # plt.scatter(t, S6)
    plt.show


solver()
# c0 = [-0.375, -0.013, -0.925, 0.411, 0.758, 0.498]
# t = np.linspace(0, 200, 100)
# print(odes(c0,0))


def ivpSol():
    x0 = [-0.375, -0.013, -0.925, 0.411, 0.758, 0.498]
    t = np.linspace(0, 200, 100)
    x = solve_ivp(odes,t,x0,method="RK45")
    print(x)


#ivpSol()






























































def SdMean():
    i = 0
    SDMEAN = np.zeros((3,3))
    for i in range(100):
        i += 1
        for m in range(3):
            for n in range(3):
                Sd = sDot1x3()
                SDMEAN[m,n]=SDMEAN[m,n]+Sd[m,n]
    #print(i)
    for m in range(3):
        for n in range(3):
            SDMEAN[m,n] = SDMEAN[m,n]/i
    print("\n" + "Matriz promediada de los cambios temporales de Espínes: \n")
    print(SDMEAN)
    return SDMEAN


#SdMean()

def solution():
    SDMEAN = SdMean()
    k1 = SDMEAN[0, 0]
    k2 = SDMEAN[0, 1]
    k3 = SDMEAN[0, 2]
    dt= np.arange(-1,100,0.25)
    e = 2.718281
    Svector1 = (3*e**((-2)*k1*dt))
    Svector2 = (e**(-2*k2*dt))
    Svector3 = (e**(-2*k3*dt))

    #SolDOT = np.sqrt(Svector1+Svector2+Svector3)
    SolDOT = np.sqrt(Svector1) + 1
    SolT = (SolDOT)/-k1 + 1 
    fig = plt.figure(figsize=(15,10))
    fig.add_subplot(1, 2, 1)
    plt.scatter(dt, SolDOT)
    plt.grid()
    plt.title("dS/dt")
    plt.xlabel("t [nanoSecs]")
    plt.ylabel("dSxs/dt")
    fig.add_subplot(1, 2, 2)
    plt.scatter(dt, SolT)
    plt.grid()
    plt.title("S(t)")
    plt.xlabel("t [nanoSecs]")
    plt.ylabel("Sx(t)")
    plt.show()


#solution()

def modulusSDMEAN():
    
    SDMEAN = SdMean()
    v1 = (SDMEAN[:, 0])
    v2 = (SDMEAN[:, 1])
    v3 = (SDMEAN[:, 2])
    mod1 = np.round(np.linalg.norm(v1), 3)
    mod2 = np.round(np.linalg.norm(v2), 3)        
    mod3 = np.round(np.linalg.norm(v3), 3)
    
    modSDMEAN = np.vstack((mod1,mod2,mod3)).T
    print("\n El modulo de la matriz meanSDOT resulta: \n")
    print(modSDMEAN)

    return modSDMEAN


#modulusSDMEAN()


def integrateAndGrafh():
    modSDMEAN = modulusSDMEAN()
    k1, k2, k3 = modSDMEAN[0, 0], modSDMEAN[0, 1], modSDMEAN[0, 2]
    dt = np.arange(0,100,step=0.05)
    
    S1 = k1*dt
    S2 = k2*dt
    S3 = k3*dt

    fig = plt.figure(figsize=(20,7))
    fig.add_subplot(1, 3, 1)
    plt.scatter(dt,S1)
    plt.title("|S1| vs time")
    plt.grid()
    plt.ylabel("|S1(t)|")
    plt.xlabel("t [nanoSecs]")
    
    fig.add_subplot(1, 3, 2)
    plt.scatter(dt, S2)
    plt.title("|S2| vs time")
    plt.grid()
    plt.ylabel("| S2(t) |")
    plt.xlabel("t [nanoSecs]")
    
    fig.add_subplot(1, 3, 3)
    plt.scatter(dt, S3)
    plt.title("|S3| vs time")
    plt.grid()
    plt.ylabel("|S3(t)|s")
    plt.xlabel("t [nanoSecs]")



    plt.show()

    return 0


#integrateAndGrafh()