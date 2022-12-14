function J_a = jacoba(S,M,q)    
J_space = jacob0(S,q);
Jws = J_space(1:3,:);
Jvs = J_space(4:6,:);
T = fkine(S,M,q,"space");
p = T(1:3,4);
J_a = -skew(p)*Jws + Jvs;
% MultiplicationMatrix = [pinv(R) zeros(3); -pinv(R)*skew(P) pinv(R)];

% R = M(1:3,1:3);
% P = M(1:3,4);
% Jws = pinv(R)*Jwb;
% Jvs = -pinv(R)*skew(P)*Jwb + pinv(R)*Jvb;
% J_a = [Jws; Jvs];
% J_a = (-skew(P) * Jwb + Jvb);

% Rsb = 1;
% for i = 1:length(S(1,:))
% %     Rsb = Rsb * twist2ht(S(:,i),q(i));
% %     Rsbtheta = Rsb(1:3,1:3);
%     Rsb = twist2ht(S(:,i),q(i));
%     Rsbtheta = Rsb(1:3,1:3);
% %     Rsbtheta = R;
% %     Rsbtheta = pinv(R);
%     r = S(1:3,i);
%     Ar = eye(3) - (1-cos(norm(r)))/(norm(r)^2) * skew(r) + ...
%     (norm(r)-sin(norm(r))/(norm(r)^3)) * (skew(r)^2);
%     qDot = [pinv(Ar) zeros(3); 
%         zeros(3) Rsbtheta];
%     J_a = [qDot*J_body(:,i) J_a];
% end

% J_space = jacob0(S,q);
% Jws = J_space(1:3,:);
% Jvs = J_space(4:6,:);
% R = M(1:3,1:3);
% P = M(1:3,4);
% % MultiplicationMatrix = [pinv(R) zeros(3); -pinv(R)*skew(P) pinv(R)];
% 
% Jwb = pinv(R)*Jws;
% Jvb = -pinv(R)*skew(P)*Jws + pinv(R)*Jvs;
% J_a = [Jwb; Jvb];
% J_a = (-skew(P) * Jws + Jvs);
% J_a = Jws;

% J_a = Jvb;

% Jws = pinv(R)*Jwb;
% Jvs = -pinv(R)*skew(P)*Jwb + pinv(R) * Jvb;
% J_a = Jvs - skew(P)*Jws;



end
