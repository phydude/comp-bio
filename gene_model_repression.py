import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint



# Set the backend for interactive plotting
plt.switch_backend('TkAgg')

# Initial conditions
y0 = [0, 0]

# Time points for simulation
t = np.linspace(0, 200, num=100)

# Model parameters
k_1 = 0.4
gamma_1 = 0.1
k_2 = 0.9
gamma_2 = 0.1
n = 4
c = 1
params = [k_1, gamma_1, k_2, gamma_2, n, c]

# Define the system of differential equations
def sim(variables, t, params):
    G1, G2 = variables
    k_1, gamma_1, k_2, gamma_2, n, c = params

    dG1dt = k_1 - gamma_1 * G1
    dG2dt = (c**n / (c**n + G1**n)) * k_2 - gamma_2 * G2

    return [dG1dt, dG2dt]

# Solve the ODEs
y = odeint(sim, y0, t, args=(params,))

# Create a visually appealing plot
plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot G1 and G2 against time
line1, = ax.plot(t, y[:, 0], color="b", label="G1")
line2, = ax.plot(t, y[:, 1], color="r", label="G2")

# Add title and labels
ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('Number', fontsize=14)

# Set axis limits and ticks
ax.set_xlim(0, 200)
ax.set_ylim(0, 1.2)
ax.set_xticks(np.arange(0, 201, 50))
ax.set_yticks(np.arange(0, 1.2, 0.2))

# Add a grid to the plot
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Add a text box with model parameters
params_text = f'Model Parameters:\nk_1={k_1}, γ_1={gamma_1}, k_2={k_2}, γ_2={gamma_2}, n={n}, c={c}'
ax.text(.3, 0.92, params_text, transform=ax.transAxes, fontsize=8, bbox=dict(facecolor='white', alpha=.8))

# Add a title and a subtitle
plt.suptitle('Simulation of G1 and G2 over Time', fontsize=22, ha='center')
plt.title('Using Ordinary Differential Equations (ODEs)', fontsize=16, ha='center')

# Adjust spacing to prevent overlapping titles
plt.subplots_adjust(top=0.85)

# Show the plot
plt.tight_layout()
plt.show()
