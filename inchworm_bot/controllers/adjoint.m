function Vs = adjoint(Va,T)
    R = T(1:3, 1:3);
    P = T(1:3,4);
    Adj = [R zeros(3);
        skew(P)*R R];
    Vs = Adj * Va;
end

