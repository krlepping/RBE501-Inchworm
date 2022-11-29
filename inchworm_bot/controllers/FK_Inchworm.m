function T = FK_Inchworm(a,b,c,d,e)
    %abcde are the joint angles for the inchworm
    S = [];
    M = [];
    T = 1;
    q = [a b c d e];
    for i = 1:length(S(1,:))
        T = T * twist2ht(S(:,i),q(i));
    end
    T = T * M;
end