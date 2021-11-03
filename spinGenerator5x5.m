function [S] = spinGenerator5x5()
    
    extremoIzq = -5;
    extremoDer = 5;
    Sz = 0;
    
    var1 = randi([extremoIzq,extremoDer],2,1);
    var2 = rand(2,1); 
    S1 = [(var1(1,1)*var2(1,1));(var1(2,1)*var2(2,1));Sz];
    
    var1 = randi([extremoIzq,extremoDer],2,1);
    var2 = rand(2,1); 
    S2 = [(var1(1,1)*var2(1,1));(var1(2,1)*var2(2,1));Sz];
    
    var1 = randi([extremoIzq,extremoDer],2,1);
    var2 = rand(2,1); 
    S3 = [(var1(1,1)*var2(1,1));(var1(2,1)*var2(2,1));Sz];
    
    var1 = randi([extremoIzq,extremoDer],2,1);
    var2 = rand(2,1); 
    S4 = [(var1(1,1)*var2(1,1));(var1(2,1)*var2(2,1));Sz];
    
    var1 = randi([extremoIzq,extremoDer],2,1);
    var2 = rand(2,1); 
    S5 = [(var1(1,1)*var2(1,1));(var1(2,1)*var2(2,1));Sz];
    
    S = [S1,S2,S3,S4,S5];
    
end