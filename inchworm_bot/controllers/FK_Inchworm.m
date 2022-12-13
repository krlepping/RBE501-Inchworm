function T = FK_Inchworm(a,b,c,d,e)
    %abcde are the joint angles for the inchworm
    S = [0 0 1 0 0 0;
        0 1 0 109.03 0 0;
        0 1 0 248.4913 -84.9940 0;
        0 1 0 109.03 -169.9879 0;
        0 0 1 0 -169.9879 0];
    M = [1 0 0 169.9879;
        0 -1 0 0;
        0 0 -1 0;
        0 0 0 1];
    T = 1;
    q = [a b c d e];
    for i = 1:length(S(1,:))
        T = T * twist2ht(S(:,i),q(i));
    end
    T = T * M;
end