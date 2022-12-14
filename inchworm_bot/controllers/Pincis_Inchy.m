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
    q0 = [0 0 0 0 0];
    startPose = fkine(S,M,q0,"space");
    q = [2*pi/100 0 0 0 0];
    
    targetResetX = [1 0 0 150; 
        0 1 0 0; 
        0 0 1 180; 
        0 0 0 1];
    targetBoxX = [0 0 -1 150; 0 1 0 0; 1 0 0 50.8; 0 0 0 1];
    targetBoxY = [0 -1 0 0; 0 0 -1 150; 1 0 0 50.8; 0 0 0 1];
    targetResetY = [1 0 0 0; 0 1 0 150; 0 0 1 180; 0 0 0 1];
    

    targetR = currPose(1:3,1:3);
    targetPose = currPose(1:3,4);
    
    currentPose = startPose(1:3,4);
    currentR = startPose(1:3,1:3);

    currentQ = [0 0 0 0 0];
    
    while norm(targetPose - currentPose) + norm(targetR - currentR) > 1e-3
        J_a = jacoba(S,M,currentQ);
        
        % Use the Levenberg-Marquadt algorithm (Damped Least Squares)
        lambda = 0.5;
        deltaQ = J_a' * pinv(J_a*J_a' + lambda^2 * eye(3)) * (targetPose - currentPose);
                    
        currentQ = currentQ + deltaQ';       
        T = fkine(S,M,currentQ,'space');
        currentPose = T(1:3,4);
    end

    