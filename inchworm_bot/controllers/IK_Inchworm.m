function [a,b,c,d,e] = IK_Inchworm(x,y,z,a,b,c,d,e,alpha,beta,gamma)
    % x y z are target x y z positions
    % a b c d e are the current positions of the gripper
    % alpha beta gamma are the xyz euler coordinates of the target position

    currentQ = [a,b,c,d,e];

    R1=[1,0,0;0,cos(alpha),-sin(alpha);0,sin(alpha),cos(alpha)]; % Rx,a
    R2=[cos(beta),0,sin(beta);0,1,0;-sin(beta),0,cos(beta)]; % Ry,b
    R3=[cos(gamma),-sin(gamma),0;sin(gamma),cos(gamma),0;0,0,1]; % Rz,c
    targetOrientation = R1*R2*R3; % Rxyz

    targetPose = [x;y;z];
    T = fkine(S_body, M, currentQ, 'body');
    
    currentPose = T(1:3,4);
    currentOrientation = T(1:3,1:3);

    S = [];
    M = [];


    while norm(targetPose - currentPose) > 1e-3 ... 
            && norm(targetOrientation - currentOrientation) > 1e-3
        J = jacoba(S,M,currentQ);
        deltaQ = J\(targetPose - currentPose);
      
        currentQ = currentQ + deltaQ';
        
        T = fkine(S,M,currentQ,false);
        currentPose = T(1:3,4);
        currentOrientation = T(1:3,1:3);
    end

    a = currentQ(1);
    b = currentQ(2);
    c = currentQ(3);
    d = currentQ(4);
    e = currentQ(5);
end