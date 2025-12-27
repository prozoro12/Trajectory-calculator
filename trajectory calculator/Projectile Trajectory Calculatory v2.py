import matplotlib.pyplot as plt
import numpy as np
from math import *

# === Input ===
angle_deg = float(input('Launch Angle (in degrees): '))
v0 = float(input('Launch Velocity (in m/s): '))
g = 9.8

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

def draw_parabola(angle, vel0, Range, hmax):
    # Example projectile data
    x = np.linspace(0, Range, 500) 
    t = x / (vel0 * cos(angle))
    yt = vel0 * sin(angle) * t - 0.5 * g * t**2
    yx = (x*tan(angle))-(g/(2*vel0*cos(angle))*(x**2))

    fig, ax = plt.subplots(figsize=(5, 6))

    ax.plot(t, yt, color='blue')
    ax.set_xlabel("X-axis (Time(s) →)")
    ax.set_ylabel("Y-axis (Height(m) ↑)")
    ax.set_title("Projectile Motion Through Time")
    ax.set_xlim(0, Range)
    ax.set_ylim(0, hmax+hmax*0.1)

    # Optional: enlarge x and y ticks
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)

    fig2, ax2 = plt.subplots(figsize=(5, 6))

    ax2.plot(x, yx, color='blue')
    ax2.set_xlabel("X-axis (Distance(m) →)")
    ax2.set_ylabel("Y-axis (Height(m) ↑)")
    ax2.set_title("Projectile Motion Through Space")
    ax2.set_xlim(0, Range)
    ax2.set_ylim(0, hmax+hmax*0.1)

    # Move the graph closer to the bottom and adjust padding
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.15)

    plt.show()

draw_parabola(angle_rad, v0, R, Hmax)
