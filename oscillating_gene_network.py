import matplotlib
matplotlib.use('tkagg')  # Using the TkAgg backend for rendering

import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np



# Initial conditions
y0 = [0, 0, 0]

# Time vector
t = np.linspace(0, 200, num=100)

# Parameters
k_1 = 0.5
gamma_1 = 0.1
k_2 = 0.5
gamma_2 = 0.1
k_3 = 0.5
gamma_3 = 0.1
n = 9
c = 1

params = [k_1, gamma_1, k_2, gamma_2, k_3, gamma_3, n, c]

# Differential equation system
def sim(variables, t, params):
    G1, G2, G3 = variables
    k_1, gamma_1, k_2, gamma_2, k_3, gamma_3, n, c = params

    dG1dt = (c**n / (c**n + G3**n)) * k_1 - gamma_1 * G1
    dG2dt = (G1**n / (c**n + G1**n)) * k_2 - gamma_2 * G2
    dG3dt = (G2**n / (c**n + G2**n)) * k_3 - gamma_3 * G3

    return [dG1dt, dG2dt, dG3dt]

# Solving the differential equations
y = odeint(sim, y0, t, args=(params,))

# Create visually stunning plots
plt.figure(figsize=(10, 8))  # Adjusting the figure size

# Plot for G1
plt.subplot(3, 1, 1)
plt.plot(t, y[:, 0], color="royalblue", label="G1")
plt.ylabel('Number of G1')
plt.title('Gene Expression Dynamics')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)  # Adding gridlines

# Plot for G2
plt.subplot(3, 1, 2)
plt.plot(t, y[:, 1], color="tomato", label="G2")
plt.ylabel('Number of G2')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)  # Adding gridlines

# Plot for G3
plt.subplot(3, 1, 3)
plt.plot(t, y[:, 2], color="limegreen", label="G3")
plt.xlabel('Time')
plt.ylabel('Number of G3')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)  # Adding gridlines

# Adjusting spacing between subplots
plt.tight_layout()

# Adding a nice background
plt.style.use('seaborn-whitegrid')

# Display the plot
plt.show()
