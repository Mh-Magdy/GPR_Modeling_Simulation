import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Setup the figure
fig, ax = plt.subplots()

# Plot the half-space (brown region) first
ax.fill_between([0, 0.480], [0.170, 0.170], [0, 0], color='#8B4513', label='Half-space (Dielectric)')

# Plot air region above the half-space
ax.fill_between([0, 0.480], [0.235, 0.235], [0.170, 0.170], color='#D3D3D3', label='Air Region')

# Plot PML region (peripheral brown region)
ax.fill_between([0, 0.480], [0.235, 0.235], [0, 0], color='#A52A2A', alpha=0.3, label='PML (Absorbing Boundary)')

# Plotting the metal cylinder in the x-z plane
cylinder = plt.Circle((0.240, 0.080), 0.010, color='black', label='Metal Cylinder', zorder=3)
ax.add_artist(cylinder)

# Set plot limits and labels for x and z axes
ax.set_xlim(0, 0.480)
ax.set_ylim(0, 0.235)
ax.set_xlabel('x (m)')
ax.set_ylabel('z (m)')
ax.set_title('B-scan Setup Visualization in X-Z Plane')

# Add legend
ax.legend(loc='upper right')

# Initial positions of the transmitter and receiver
transmitter_pos = 0.105
receiver_pos = 0.110
z_pos = 0.170  # Fixed z-position

# Plot initial transmitter and receiver
transmitter, = ax.plot(transmitter_pos, z_pos, 'ro', label='Transmitter', markersize=8, zorder=4)
receiver, = ax.plot(receiver_pos, z_pos, 'bo', label='Receiver', markersize=8, zorder=4)

# Animation function to update transmitter and receiver positions
def animate(i):
    # Move the transmitter and receiver incrementally to the right
    transmitter.set_data(transmitter_pos + i*0.005, z_pos)
    receiver.set_data(receiver_pos + i*0.005, z_pos)
    return transmitter, receiver

# Number of frames will be determined by how many steps it takes for the receiver to reach the end
num_frames = int((0.480 - receiver_pos) / 0.005)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=100, blit=True)

# Show the plot with animation
plt.show()

