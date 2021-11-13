function [] = FINAL()
    pkg load symbolic;
    
    syms S1(t) S2(t) S3(t) S4(t) S5(t) S6(t);
    
    cond = [S1(0) == -0.375,S2(0) == -0.013,S3(0) == -0.925,S4(0) == 0.411,S5(0) == 0.758,S6(0) == 0.498];
    
    dS1 = diff(S1,t) == S2*S6 + 2*S3*S5;
    dS2 = diff(S2,t)== -2*S3*S4 - S1*S6;
    dS3 = diff(S3,t)== -2*S1*S5 + 2*S2*S4;
    dS4 = diff(S4,t)== S5*S3 - 2*S6*S2;
    dS5 = diff(S5,t)== -2*S6*S1 - S4*S3;
    dS6 = diff(S6,t)== -2*S4*S2 + 2*S5*S1;
    
    eqns = [dS1,dS2,dS3,dS4,dS5,dS6];
    
    S = dsolve(eqns,cond)
    
    t= linspace(0,100,250)
end