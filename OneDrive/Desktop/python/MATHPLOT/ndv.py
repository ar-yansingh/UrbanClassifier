# Generate a Bode phase plot for the same RLC second-order system
import numpy as np
import matplotlib.pyplot as plt

# Parameters from earlier calculation
K = 1.0
zeta = 0.24
wn = 3.12e6  # rad/s

# Frequency range
w = np.logspace(4, 8, 500)

# Phase calculation for G(jw)
phase = -np.arctan2(2*zeta*wn*w, (wn**2 - w**2))
phase_deg = np.degrees(phase)

# Plot phase
plt.figure()
plt.semilogx(w, phase_deg)
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Phase (degrees)")
plt.title("Bode Phase Plot for Experimental RLC System")
plt.grid(True, which="both")
plt.show()
