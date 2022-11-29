function R = axisangle2rot(omega,theta)
    omega_ss = [0 -omega(3) omega(2); omega(3) 0 -omega(1); -omega(2) omega(1) 0];
    R = eye(3) + sin(theta) * omega_ss + (1 - cos(theta)) * omega_ss^2;
end