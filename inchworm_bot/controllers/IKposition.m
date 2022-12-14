function q = IKposition(S,M,currentT,targetT,currentQ)
    targetR = targetT(1:3,1:3);
    targetPose = targetT(1:3,4);
    
    currentPose = currentT(1:3,4);
    currentR = currentT(1:3,1:3);
    k = 0.1;
    
%     while norm(targetPose - currentPose) + norm(targetR - currentR) > 1e-3
    while norm(targetPose - currentPose) > 1e-5
        J_0 = jacob0(S,currentQ);
        J_a = jacoba(S,M,currentQ);
        
        % Use the Levenberg-Marquadt algorithm (Damped Least Squares)
        lambda = 0.5;
%         rotation_error = targetR - currentR % Trying to use the rotation
%         error but can't find an equation that will work
%         theta = acos((cos(rotation_error(1,1)+cos(rotation_error(2,2))+cos(rotation_error(3,3)))-1)/2);
%         n = 1/(2*sin(theta))*[cos(rotation_error(3,2))-cos(rotation_error(2,3));cos(rotation_error(1,3))-cos(rotation_error(3,1));cos(rotation_error(2,1))-cos(rotation_error(1,2))];
%         phi = theta*n;
%         J = jacob0(S,currentQ);
%         deltaQ_Rotation = J_a' * pinv(J_a * J_a') * phi;
%         deltaQ = J_a' * pinv(J_a*J_a' + lambda^2 * eye(3)) * poseError + deltaQ_Rotation;

%         generalized coordinates results in rotationo matrix using basic
%         coordinate and xyz euler : 

%         deltaQ = J_a' * pinv(J_a*J_a' + lambda^2 * eye(3)) * (targetPose - currentPose);

        % Numerical Inverse?
%         z = [1 1 1 1 1]';
%         y = pinv(J_0'*J_0)*J_0' * z;
%         deltaQ = y*(targetPose - currentPose);

%         deltaQ = pinv(J_0'*J_0)*J_0' * (targetPose - currentPose);

        
                    
        currentQ = currentQ + deltaQ';
        T = fkine(S,M,currentQ,'space');
        currentPose = T(1:3,4);
%         currentR = T(1:3,1:3)
%         targetR
    end
    q = currentQ;
end