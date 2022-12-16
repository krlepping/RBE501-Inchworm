function Pincis_Inchy()
    % Considering our robot is a RRPRR
%     S = [0 0 1 0 0 0; % Done Ninja way and cross product way
%         1 0 0 0 109.03 0;
%         0 0 0 0 0 0;
%         1 0 0 0 109.03 -169.9879;
%         0 0 1 0 0 -169.9879]';
    
    % Considering our robot is an RRRRR
    S = [0 0 1 0 0 0;
        1 0 0 0 109.03 0;
        1 0 0 0 248.4913 -84.9940;
        1 0 0 0 109.03 -169.9879;
        0 0 1 0 0 -169.9879]'
    M = [1 0 0 0;
        0 1 0 169.9879;
        0 0 1 0;
        0 0 0 1];
    q0 = [0 0 0 0 0];
    startPose = fkine(S,M,q0,"space")
    
    targetResetX = [1 0 0 150; 
                    0 1 0 0; 
                    0 0 1 180; 
                    0 0 0 1];
    targetBoxY = [0 0 -1 0; 
                  0 1 0 300; 
                  1 0 0 50.8; 
                  0 0 0 1];
    targetBoxX = [0 -1 0 300; 
                  0 0 -1 0; 
                  1 0 0 50.8; 
                  0 0 0 1];
    targetResetY = [1 0 0 0; 0 1 0 150; 0 0 1 180; 0 0 0 1];
    
    %% Get first Y reset (go to a point that won't hit any boxes
    position1 = IKposition(S,M,startPose,targetResetY,q0)

    %% Trajectory code for q0 to position 1 here

    %% Get Y target
    position2 = IKposition(S,M,targetResetY,targetBoxY,position1)
    %% Trajectory code for position1 to position2 here

    %% Get X reset
    position3 = IKposition(S,M,targetBoxY,targetResetX,position2)
    %% Trajectory code for position2 to position3 here

    %% Get X target
    position4 = IKposition(S,M,targetResetX,targetBoxX,position3)
    %% Trajectory code for position3 to position 4 here


