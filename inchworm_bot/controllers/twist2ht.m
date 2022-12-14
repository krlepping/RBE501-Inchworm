function T = twist2ht(S,theta)
R = axisangle2rot(S(1:3),theta);
        ah_FUCK = (eye(3) * theta + (1 - cos(theta)) * skew(S(1:3)) + ...
            (theta - sin(theta))*(skew(S(1:3))^2))*S(4:6);
    T = [R ah_FUCK
        0 0 0 1];
end