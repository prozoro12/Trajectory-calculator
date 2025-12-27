#FILE TO BE IMPORTED

import matplotlib.pyplot as plt
import numpy as np
from math import *

# === Input ===
#angle_deg = float(input('Launch Angle (in degrees): '))
#v0 = float(input('Launch Velocity (in m/s): '))

#g = 9.8
'''
# === Calculations ===
angle_rad = radians(angle_deg)
v0x = v0 * cos(angle_rad)
v0y = v0 * sin(angle_rad)

T = (2 * v0y) / g
R = v0x * T
Hmax = (v0y ** 2) / (2 * g)

print(f'\nInitial Vertical Velocity: {v0y:.2f} m/s')
print(f'Initial Horizontal Velocity: {v0x:.2f} m/s')
print(f'Total Flight Time (T): {T:.2f} s')
print(f'Total Range (R): {R:.2f} m')
print(f'Maximum Height (Hmax): {Hmax:.2f} m')
'''
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, tan, radians

g = 9.8

def draw_parabola(angle_deg, vel0, g):
    # Convert angle to radians
    angle = radians(angle_deg)

    # Compute range and max height
    Range = (vel0**2 * np.sin(2 * angle)) / g
    hmax = (vel0**2 * np.sin(angle)**2) / (2 * g)

    # === Normal Lines ===
    nx = np.linspace(-2*Range, 2*Range, 3)
    nt = np.linspace(-2*(2 * vel0 * np.sin(angle)), 2*(2 * vel0 * np.sin(angle)), 3)
    ny = np.linspace(-2*Range, 2*Range, 3)
    
    # === Through Time ===
    t = np.linspace(0, 2*(2 * vel0 * np.sin(angle)) / g, 500)
    yt = vel0 * np.sin(angle) * t - 0.5 * g * t**2

    # === Through Space ===
    x = np.linspace(0, 2*Range, 500)
    yx = x * np.tan(angle) - (g * x**2) / (2 * vel0**2 * np.cos(angle)**2)

    # === Figure 1: Height vs Time ===
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(t, yt, color='blue')
    ax.plot(nt, nt * 0, color='black')
    ax.plot(ny * 0, ny, color='black')
    ax.set_xlabel("Time (s) →")
    ax.set_ylabel("Height (m) ↑")
    ax.set_title("Projectile Motion: Height vs Time")
    ax.set_xlim(0, t[-1])
    ax.set_ylim(0, hmax * 1.1)
    ax.grid(True)
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    fig.tight_layout(pad=1.5)

    # === Figure 2: Height vs Distance ===
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    ax2.plot(x, yx, color='blue')
    ax2.plot(nx, nx * 0, color='black')
    ax2.plot(ny * 0, ny, color='black')
    ax2.set_xlabel("Distance (m) →")
    ax2.set_ylabel("Height (m) ↑")
    ax2.set_title("Projectile Motion: Height vs Distance")
    ax2.set_xlim(0, Range)
    ax2.set_ylim(0, hmax * 2.2)
    #ax2.set_aspect('equal', adjustable='box')
    ax2.grid(True)
    ax2.tick_params(axis='x', labelsize=10)
    ax2.tick_params(axis='y', labelsize=10)
    fig2.tight_layout(pad=1.5)

    plt.show()
