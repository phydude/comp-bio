import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

# Initial conditions and time points for simulation
y0 = [0, 0]
t = np.linspace(0, 200, num=100)

# Define parameters for the simulation
k_1 = 0.5
gamma_1 = 0.1
k_2 = 0.5
gamma_2 = 0.05
n = 5
c = 5

# Pack parameters into a list for use in the simulation function
params = [k_1, gamma_1, k_2, gamma_2, n, c]

# Define the system of differential equations for the simulation
def sim(variables, t, params):
    G1 = variables[0]
    G2 = variables[1]

    k_1 = params[0]
    gamma_1 = params[1]
    k_2 = params[2]
    gamma_2 = params[3]
    n = params[4]
    c = params[5]

    dG1dt = k_1 - gamma_1 * G1
    dG2dt = (G1**n / (c**n + G1**n)) * k_2 - gamma_2 * G2

    return [dG1dt, dG2dt]

# Solve the differential equations using odeint
y = odeint(sim, y0, t, args=(params,))

# Create a figure and axes for the plot
f, ax = plt.subplots(1)

# Plot the results for G1 and G2 over time
line1, = ax.plot(t, y[:, 0], color="b", label="G1")
line2, = ax.plot(t, y[:, 1], color="r", label="G2")

# Set labels for the axes and a legend
ax.set_ylabel('Number of Molecules')
ax.set_xlabel('Time')
ax.legend(handles=[line1, line2])

# Add a title to the plot
plt.title('Simulation of Molecular Concentrations over Time')

# Set a grid for better visualization
plt.grid(True)

# Set a background color for the plot
ax.set_facecolor('#f0f0f0')

# Customize the legend
ax.legend(loc='upper right', fontsize='medium', fancybox=True, shadow=True)

# Add a border around the plot
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(0.5)
    spine.set_edgecolor('black')

# Show the plot
plt.show()
