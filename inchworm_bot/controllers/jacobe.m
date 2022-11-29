function J_v = jacobe(S,M,q)    
J_v = [];
T = 1;
l = length(q)+1;
R = M(1:3,1:3);
    for i = 1 : length(q)
        temp = pinv(twist2ht(S(:,l-i),q(l-i)));
        T = T * temp;
        if(i ~= 1)
            adj = adjoint(S(:,l-i),T);
            J_v = [adj J_v];
        else
           J_v = [S(:,l-i)];
        end
    end
end
