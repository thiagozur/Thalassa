import numpy as np
from python.models.sound_speed import c_mackenzie

class OceanProfile:
    def __init__(self, known_depths, known_sal, known_temp):
        if not len(known_depths) == len(known_sal) == len(known_temp):
            raise ValueError("Data ranges are not equal")
        if len(known_depths) < 2:
            raise ValueError("Insufficient data")
        if any(n < 0 for n in known_depths) or any(n < 0 for n in known_sal):
            raise ValueError("Negative values for salinity or depth are not valid")
        if not all(x < y for x, y in zip(known_depths, known_depths[1:])):
            raise ValueError("Depth values are not strictly increasing")

        self.depth = np.array(known_depths, dtype = float, copy = True)
        self.salinity = np.array(known_sal, dtype = float, copy = True)
        self.temperature = np.array(known_temp, dtype = float, copy = True)

        if not np.all(np.isfinite(self.depth)) or not np.all(np.isfinite(self.salinity)) or not np.all(np.isfinite(self.temperature)):
            raise ValueError("Invalid data")

    def _validate_depth(self, d):
        if not np.isfinite(d):
            raise ValueError("Invalid depth")
        if d < self.depth[0] or d > self.depth[-1]:
            raise ValueError("Depth outside profile range")
    
    def get_temperature(self, d):
        self._validate_depth(d)
        return np.interp(d, self.depth, self.temperature)
        
    def get_salinity(self, d):
        self._validate_depth(d)
        return np.interp(d, self.depth, self.salinity)

    def get_sound_speed(self, d):
        temp = self.get_temperature(d)
        sal = self.get_salinity(d)
        return c_mackenzie(d, sal, temp)