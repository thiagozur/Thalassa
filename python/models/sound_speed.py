from math import isfinite

def c_mackenzie(depth, salinity, temperature):
    try:
        d = float(depth)
        s = float(salinity)
        t = float(temperature)
    except (ValueError, TypeError):
        raise ValueError("Invalid inputs")

    if not isfinite(d) or not isfinite(s) or not isfinite(t):
        raise ValueError("Invalid inputs")

    if d < 0 or d > 8000:
        raise ValueError("Depth outside valid range")
    
    if s < 25 or s > 40:
        raise ValueError("Salinity outside of valid range")

    if t < 2 or t > 30:
        raise ValueError("Temperature outside of valid range")

    return 1448.96 + 4.591 * t - 0.05304 * t * t + 0.0002374 * t * t * t + 1.34 * (s - 35) + 0.0163 * d + 0.0000001675 * d * d - 0.01025 * t * (s - 35) - 0.0000000000007139 * t * d * d * d