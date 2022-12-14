function is_it = inWorkspace(x,y,z)
sphere_start = [0 0 109.03]';
sphere_radius = 163.32 + 163.71 + 108.70;
if((x-sphere_start(1))^2+(y-sphere_start(2))^2+(z-sphere_start(3))^2 <= sphere_radius^2)
    is_it = true;
else
    is_it = false;
end
end