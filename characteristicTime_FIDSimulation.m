function [tau] = characteristicTime_FIDSimulation(SMean,J)
    
    S = SMean;
    
    for n = 1:5
        for m = 1:1
            tau(m,n) = 1/(sqrt((pow2(J(m,n))*pow2(S(1,n)) + pow2(J(m,n))*pow2(S(2,n)) + pow2(J(m,n))*pow2(S(3,n)))));
        endfor
    endfor
    
end