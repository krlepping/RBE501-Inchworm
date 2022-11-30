function [a,b,c,d,e] = IK_InchwormNoOrientation(x,y,z,a,b,c,d,e)
    % x y z are target x y z positions
    % a b c d e are the current positions of the gripper
    % alpha beta gamma are the xyz euler coordinates of the target position

    S = [];
    M = [];

    currentQ = [a,b,c,d,e];

    targetPose = [x;y;z];
    T = fkine(S, M, currentQ, 'body');
    
    currentPose = T(1:3,4);

    while norm(targetPose - currentPose) > 1e-3
        J = jacoba(S,M,currentQ);
        deltaQ = J\(targetPose - currentPose);
      
        currentQ = currentQ + deltaQ';
        
        T = fkine(S,M,currentQ,false);
        currentPose = T(1:3,4);
    end

    a = currentQ(1);
    b = currentQ(2);
    c = currentQ(3);
    d = currentQ(4);
    e = currentQ(5);
end