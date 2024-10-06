import matplotlib.pyplot as plt
import numpy as np

# Setup the figure
fig, ax = plt.subplots()

# Plot the half-space (brown region) first
# Half-space occupies the region below z = 0.170 in the x-z plane
ax.fill_between([0, 0.480], [0.170, 0.170], [0, 0], color='#8B4513', label='Half-space (Dielectric)')

# Plot air region above the half-space
ax.fill_between([0, 0.480], [0.235, 0.235], [0.170, 0.170], color='#D3D3D3', label='Air Region')

# Plot PML region (peripheral brown region)
ax.fill_between([0, 0.480], [0.235, 0.235], [0, 0], color='#A52A2A', alpha=0.3, label='PML (Absorbing Boundary)')

# Plotting the metal cylinder in the x-z plane
# The cylinder is centered at x = 0.240, z = 0.080 with a radius of 0.010
cylinder = plt.Circle((0.240, 0.080), 0.010, color='black', label='Metal Cylinder', zorder=3)
ax.add_artist(cylinder)

# Plotting transmitter and receiver in the x-z plane
# Transmitter is located at (0.105, 0.170) in the x-z plane
# Receiver is located at (0.110, 0.170), displaced by 5 mm in the x direction
plt.plot(0.105, 0.170, 'ro', label='Transmitter', markersize=8, zorder=4)  # Transmitter
plt.plot(0.110, 0.170, 'bo', label='Receiver', markersize=8, zorder=4)    # Receiver

# Set plot limits and labels for x and z axes
ax.set_xlim(0, 0.480)
ax.set_ylim(0, 0.235)
ax.set_xlabel('x (m)')
ax.set_ylabel('z (m)')
ax.set_title('B-scan Setup Visualization in X-Z Plane')

# Add legend
ax.legend(loc='upper right')

# Show plot
plt.show()

