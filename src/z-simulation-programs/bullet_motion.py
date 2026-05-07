import math
import matplotlib.pyplot as plt

# Initial conditions
v0 = 800              # initial velocity (m/s)
angle = 30            # degrees
g = -9.81             # gravity (m/s^2)

# Convert angle to radians
theta = math.radians(angle)

# Initial velocity components
vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)

# Initial position
x, y = 0, 0

# Time step
dt = 0.01

# Store trajectory
x_vals = []
y_vals = []

# Simulation loop
while y >= 0:
    x_vals.append(x)
    y_vals.append(y)

    # Update position
    x += vx * dt
    y += vy * dt

    # Update velocity
    vy += g * dt

# Plot the trajectory
plt.plot(x_vals, y_vals)
plt.title("Bullet Trajectory (No Air Resistance)")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid()
plt.show()