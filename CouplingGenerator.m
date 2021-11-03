function [J] = CouplingGenerator(S) 
    % Constantes:
    r0 = 2.72e-10; % [m]
    g = 25166.2; % [Rad/sOe]
    h  = 6.582e-16; % [J.s]%HBAR%    
    J = [];
    for n = 1:5
        for m = 1:5
            thetaFactor = ((S(1,n)*S(1,m))+(S(2,n)*S(2,m)))*((S(1,n)*S(1,m))+(S(2,n)*S(2,m)));
            J(m,n) = ((g*g*h*h)-(((-3))*(g*g*h*h)*(thetaFactor)))/((-2)*r0*r0*r0);
        endfor
    endfor    
    
end