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
    
    targetResetX = [1 0 0 150; 
        0 1 0 0; 
        0 0 1 180; 
        0 0 0 1];
    targetBoxX = [0 0 -1 150; 0 1 0 0; 1 0 0 50.8; 0 0 0 1];
    targetBoxY = [0 -1 0 0; 0 0 -1 150; 1 0 0 50.8; 0 0 0 1];
    targetResetY = [1 0 0 0; 0 1 0 150; 0 0 1 180; 0 0 0 1];
    
    position1 = IKposition(S,M,startPose,targetResetX,q0);



