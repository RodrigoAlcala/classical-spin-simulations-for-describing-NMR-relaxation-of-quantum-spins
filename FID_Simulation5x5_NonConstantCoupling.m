function [Sdot] = FID_Simulation5x5_NonConstantCoupling()
    % Autor: Rodrigo N. Alcalá M.
    % Licencia: General Public License V3
    % Simulación Spin-Lattice en CaF_2, sistema 5x5
    
    % Constantes:
    r0 = 2.72e-10; % [m]
    g = 25166.2; % [Rad/sOe]
    h  = 6.582e-16 % [eV.s]%HBAR%
 
    %J = ((g*g*h*h)-(((-3))*(g*g*h*h)*(thetaFactor)))/((-2)*r0*r0*r0)
    
    
    leftFactor = 5;
    rightFactor = 1;
    upFactor = 5;
    downFactor = 1;
    
    S = spinGenerator5x5();
    Sdot = [];
    J = CouplingGenerator(S); 
    
    %timeChar = 1/sqrt()
    
    
    for n = 1:5
        for m = 1:5
            
            left  = (n-1);
            right = (n+1);
            up = (m-1);
            down = (m+1);
            
            if left == 0
                
                left = 5;
                
                xFactor = (S(1,m))*(J(m,n))*(2*S(2,n) + S(2,left) + S(2,right));
                yFactor = (S(2,m))*(J(m,n))*(2*S(1,n) + S(1,left) + S(1,right));
            
                Sdot(m,n) = xFactor - yFactor;    
                
            elseif right == 6
                
                right = 1;
                
                xFactor = (S(1,m))*(J(m,n))*(2*S(2,n) + S(2,left) + S(2,right));
                yFactor = (S(2,m))*(J(m,n))*(2*S(1,n) + S(1,left) + S(1,right));
                
                Sdot(m,n) = xFactor - yFactor;
            else
                xFactor = (S(1,m))*(J(m,n))*(2*S(2,n) + S(2,left) + S(2,right));
                yFactor = (S(2,m))*(J(m,n))*(2*S(1,n) + S(1,left) + S(1,right));
                Sdot(m,n) = xFactor - yFactor;
            end
            
        endfor
    endfor    
    
    
end   