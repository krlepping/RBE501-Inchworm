function generateWorkspaceSphere()
    [x,y,z] = sphere;
    sphere_start = [0 0 109.03]';
    sphere_radius = 163.32 + 163.71 + 108.70;
    x = x*sphere_radius;
    y = y*sphere_radius;
    z = z*sphere_radius;
    surf(x + sphere_start(1), y + sphere_start(2), z + sphere_start(3))

