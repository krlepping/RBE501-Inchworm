function Pincis_Inchy()
    S = [0 0 1 0 0 0;
        0 1 0 109.03 0 0;
        0 1 0 248.4913 -84.9940 0;
        0 1 0 109.03 -169.9879 0;
        0 0 1 0 -169.9879 0]';
    M = [1 0 0 169.9879;
        0 -1 0 0;
        0 0 -1 0;
        0 0 0 1];
    q = [2*pi/100 0 0 0 0];
    currPose = fkine(S,M,q,"space");
    targetPose = currPose(1:3,4);

    targetR = currPose(1:3,1:3);
    
    while norm(targetPose - currentPose) > 1e-3
        J_a = jacoba(S,M,currentQ);
        
        % Use the Levenberg-Marquadt algorithm (Damped Least Squares)
        lambda = 0.5;
        deltaQ = J_a' * pinv(J_a*J_a' + lambda^2 * eye(3)) * (targetPose - currentPose);
                    
        currentQ = currentQ + deltaQ';       
        T = fkine(S,M,currentQ,'space');
        currentPose = T(1:3,4);
    end
    
    