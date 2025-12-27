from math import *
import turtle as t

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

# === Turtle Setup ===
# Dynamically adjust window based on range and height
screen_width = int(R * 15) + 100   # 50px extra margin on both sides
screen_height = int(Hmax * 20) + 200
screen_width = max(screen_width, 900)
screen_height = max(screen_height, 600)

t.setup(width=screen_width, height=screen_height)
t.title("Projectile Motion")

# Set world coordinates so graph sits lower
x_margin = R * 0.05
y_margin_top = Hmax * 0.3
y_margin_bottom = Hmax * 0.3  # more space below for labels
t.setworldcoordinates(-x_margin, -y_margin_bottom, R + x_margin, Hmax + y_margin_top)

t.speed(0)
t.hideturtle()

# === Draw Axes ===
t.pensize(2)
t.color("black")

# X-axis
t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()
t.forward(R + x_margin)
t.penup()
t.goto(R + x_margin * 0.4, (-Hmax * 0.8))  # slightly below
t.write("X-axis (Range →)", font=("Arial", 11, "normal"))

# Y-axis
t.penup()
t.goto(0, 0)
t.setheading(90)
t.pendown()
t.forward(Hmax + y_margin_top)
t.penup()
t.goto((-R * 0.08)-5, Hmax + y_margin_top * 0.2)
t.write("Y-axis (Height ↑)", font=("Arial", 11, "normal"))

# === Axis Ticks & Labels ===
t.pensize(1)
t.color("black")

# X-axis ticks
num_ticks_x = 10
for i in range(num_ticks_x + 1):
    x = i * (R / num_ticks_x)
    t.penup()
    t.goto(x, 0)
    t.setheading(90)
    t.pendown()
    t.forward(Hmax * 0.01)
    t.penup()
    t.goto(x, -Hmax * 0.07)
    t.write(f"{x:.1f}", align="center", font=("Arial", 9, "normal"))

# Y-axis ticks
num_ticks_y = 8
for j in range(num_ticks_y + 1):
    y = j * (Hmax / num_ticks_y)
    t.penup()
    t.goto(0, y)
    t.setheading(0)
    t.pendown()
    t.forward(R * 0.01)
    t.penup()
    t.goto(-R * 0.07, y - Hmax * 0.015)
    t.write(f"{y:.1f}", align="right", font=("Arial", 9, "normal"))

# === Draw Projectile Path ===
t.penup()
t.goto(0, 0)
t.pendown()
t.color("blue")
t.pensize(1)

steps = 100
for i in range(steps + 1):
    time = i * (T / steps)
    x = v0x * time
    y = v0y * time - 0.5 * g * time ** 2
    t.goto(x, y)

t.done()
