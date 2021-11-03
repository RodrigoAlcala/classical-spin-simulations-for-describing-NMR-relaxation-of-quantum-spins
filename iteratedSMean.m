function [SMean] = iteratedSMean(iter=500)    % Autor: Rodrigo N. Alcalá M.    % Licencia: General Public License V3    % Simulación FID en CaF_2, sistema 5x5        SIter = [];    SMean = [];    iterPoints = [];        for i = 1:iter        S = spinGenerator5x5();        SIter = cat(3,SIter,S);
    endfor
        for n = 1:5        for m = 1:3            iterPoints = SIter(m,n,:);            SMean(m,n) = (mean(iterPoints));
        endfor
    endfor
