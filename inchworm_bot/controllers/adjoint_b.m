function Vb = adjoint_b(Va,T)
    R = T(1:3, 1:3);
    P = T(1:3,4);
    Adj = [pinv(R) zeros(3);
        -pinv(R)*skew(P) pinv(R)];
    Vb = Adj * Va;
end