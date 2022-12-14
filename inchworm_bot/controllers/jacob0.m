function J = jacob0(S,q)
J = [];
T = 1;
    for i = 1 : length(q)
        temp = twist2ht(S(:,i),q(i));
        T = T * temp;
        if(i ~= 1)
            adj = adjoint(S(:,i),T);
            J = [J adj];
        else
           J = [S(:,i)];
        end
    end
end