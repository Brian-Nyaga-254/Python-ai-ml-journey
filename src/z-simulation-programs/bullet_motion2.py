import math
import matplotlib.pyplot as plt

# Constants
v0 = 800
angle = 30
g = -9.81

Cd = 0.295      # drag coefficient
rho = 1.225     # air density (kg/m^3)
A = 0.0001      # cross-sectional area (m^2)
mass = 0.01     # bullet mass (kg)

theta = math.radians(angle)

vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)

x, y = 0, 0
dt = 0.01

x_vals = []
y_vals = []

while y >= 0:
    x_vals.append(x)
    y_vals.append(y)

    # Speed
    v = math.sqrt(vx**2 + vy**2)

    # Drag force
    Fd = 0.5 * Cd * rho * A * v**2

    # Acceleration
    ax = -Fd * vx / (v * mass)
    ay = g - (Fd * vy / (v * mass))

    # Update velocity
    vx += ax * dt
    vy += ay * dt

    # Update position
    x += vx * dt
    y += vy * dt

# Plot
plt.plot(x_vals, y_vals)
plt.title("Bullet Trajectory (With Air Resistance)")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid()
plt.show()