function q = IKposition(S,M,currentT,targetT,currentQ)
    targetR = targetT(1:3,1:3);
    targetPose = targetT(1:3,4);
    
    currentPose = currentT(1:3,4);
    currentR = currentT(1:3,1:3);
    
    while norm(targetPose - currentPose) + norm(targetR - currentR) > 1e-3
        J_a = jacoba(S,M,currentQ);
        
        % Use the Levenberg-Marquadt algorithm (Damped Least Squares)
        lambda = 0.5;
        rotation_error = targetR - currentR;
        k = 0.1;
        J0 = jacob0(S,currentQ);
        deltaQ_Rotation = currentQ * rotation_error;
        deltaQ = J_a' * pinv(J_a*J_a' + lambda^2 * eye(3)) * (targetPose - currentPose);
                    
        currentQ = currentQ + deltaQ';
        T = fkine(S,M,currentQ,'space');
        currentPose = T(1:3,4);
    end
    q = currentQ;
end