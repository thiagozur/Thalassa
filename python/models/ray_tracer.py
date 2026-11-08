import math
import numpy as np

def trace_ray(x0pos, z0pos, theta0val, sound_speed, duration, delta_t):
    try:
        x0 = float(x0pos)
        z0 = float(z0pos)
        theta0 = float(theta0val)
        c = float(sound_speed)
        d = float(duration)
        dt = float(delta_t)
    except (ValueError, TypeError):
        raise ValueError("Invalid inputs")
    if not math.isfinite(x0) or not math.isfinite(z0) or not math.isfinite(theta0) or not math.isfinite(c) or not math.isfinite(d) or not math.isfinite(dt):
        raise ValueError("Invalid inputs")
    if dt <= 0:
        raise ValueError("Time step must be positive")
    if d <= 0:
        raise ValueError("Duration must be a positive")
    if c <= 0:
        raise ValueError("Sound speed must be a positive")
    if z0 < 0:
        raise ValueError("Depth must be underwater")
    
    x = [x0]
    z = [z0]

    elapsed = 0
    while elapsed < d:
        step = min(dt, d - elapsed)
        
        x.append(x[-1] + c * math.cos(theta0) * step)
        z.append(z[-1] + c * math.sin(theta0) * step)
        
        elapsed += step

    return np.array(x), np.array(z)
