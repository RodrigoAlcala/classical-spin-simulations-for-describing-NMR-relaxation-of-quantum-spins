function [SDotMean] = iterated_SDOT_Mean(iter=500)
    % Autor: Rodrigo N. Alcalá M.
    % Licencia: General Public License V3
    % Simulación FID en CaF_2, sistema 5x5
    
    SDotIter = [];
    SDotMean = [];
    iterPoints = [];
    
    for i = 1:iter
        [Sdot] = FID_Simulation5x5_ConstantCoupling();
        SDotIter = cat(3,SDotIter,Sdot);
    endfor

    
    for n = 1:5
        for m = 1:3
            iterPoints = SDotIter(m,n,:);
            SDotMean(m,n) = (mean(iterPoints));
        endfor
    endfor
