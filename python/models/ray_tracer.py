import math
import numpy as np
from python.environment.ocean_profile import OceanProfile

def trace_ray(x0pos, z0pos, theta0val, ocean_profile: OceanProfile, duration, delta_t):
    if not isinstance(ocean_profile, OceanProfile):
        raise TypeError("Invalid ocean profile")
    try:
        x0 = float(x0pos)
        z0 = float(z0pos)
        theta0 = float(theta0val)
        d = float(duration)
        dt = float(delta_t)
    except (ValueError, TypeError):
        raise ValueError("Invalid inputs")
    if not math.isfinite(x0) or not math.isfinite(z0) or not math.isfinite(theta0) or not math.isfinite(d) or not math.isfinite(dt):
        raise ValueError("Invalid inputs")
    if dt <= 0:
        raise ValueError("Time step must be positive")
    if d <= 0:
        raise ValueError("Duration must be positive")
    if z0 < ocean_profile.depth[0] or z0 > ocean_profile.depth[-1]:
        raise ValueError("Depth must be inside the ocean profile limits")
    
    x = [x0]
    z = [z0]
    theta = [theta0]

    elapsed = 0
    while elapsed < d:
        step = min(dt, d - elapsed)

        czn = ocean_profile.get_sound_speed(z[-1])
        cos_theta = math.cos(theta[-1])
        g = ocean_profile.get_sound_speed_gradient(z[-1])
        dx = czn * cos_theta
        dz = czn * math.sin(theta[-1])
        dtheta = -g * cos_theta

        new_z = z[-1] + dz * step
        if new_z < ocean_profile.depth[0] or new_z > ocean_profile.depth[-1]:
            raise ValueError("Ray left the ocean profile limits")
        x.append(x[-1] + dx * step)
        z.append(new_z)
        theta.append(theta[-1] + dtheta * step)
        
        elapsed += step

    return np.array(x), np.array(z), np.array(theta)
