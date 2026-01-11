"""
Sattelite re-entry calculator.
Author: Jits Doomen.
Description: Will calculate whether or not a sattelite will naturally de-orbit in a span of 5 years.
"""


import math

# 2. CONSTANTS
GRAVITY_CONSTANT = 6.6743e-11
EARTH_MASS = 5.9722e24
EARTH_RADIUS = 6378137
AIR_AT_SEA_LEVEL = 1.225
ACH = 8500

# 3. ATMOSPHERIC MODEL FUNCTION
def calculate_density(alt_meters):
    rho = AIR_AT_SEA_LEVEL * math.exp(-alt_meters / ACH)
    return rho

# 4. ORBITAL VELOCITY FUNCTION
def calculate_velocity(alt_meters):
    r = EARTH_RADIUS + alt_meters
    v = math.sqrt(EARTH_MASS * GRAVITY_CONSTANT / r)
    return v

# 5. DRAG FORCE FUNCTION
def calculate_drag(rho, v, area):
    CD = 2.2
    FD = 0.5 * rho * v**2 * CD * area
    return FD

# 6. USER INPUT & DATA PROCESSING
ALTITUDE_KM = float(input("Enter altitude in km: "))
SATTELITE_MASS = float(input("Enter satellite mass in kg: "))
SATTELITE_AREA = float(input("Enter cross-section area in m^2: "))
altitude_m = ALTITUDE_KM * 1000

d = calculate_density(altitude_m)
vel = calculate_velocity(altitude_m)
f = calculate_drag(d, vel, SATTELITE_AREA)

# 7. THE AUDITOR REPORT
print(f"The calculated drag force is: {f} Newtons.")

if f <= 1e-12:
    print("This sattelite will not re-enter in the 5 year time limit from ESA.")
else:
    print("This sattelite will re-enter in the 5 year time limit from ESA.")
