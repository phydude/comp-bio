import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Initial conditions
y0 = [0, 0]  # 0 mRNA, 0 protein

# Time vector
t = np.linspace(0, 200, num=100)

# Model parameters
k_m = 0.2
gamma_m = 0.05
k_p = 0.4
gamma_p = 0.1

params = [k_m, gamma_m, k_p, gamma_p]

# Define the simulation function
def sim(variables, t, params):
    m = variables[0]
    p = variables[1]

    k_m = params[0]
    gamma_m = params[1]
    k_p = params[2]
    gamma_p = params[3]

    dmdt = k_m - gamma_m * m
    dpdt = k_p * m - gamma_p * p

    return [dmdt, dpdt]

# Perform the simulation
y = odeint(sim, y0, t, args=(params,))

# Create the plot
fig, ax = plt.subplots(1)

# Plot mRNA (M) with a dark blue solid line
line1, = ax.plot(t, y[:, 0], color="#005B9F", linestyle="-", linewidth=2, label="mRNA (M)")

# Plot protein (P) with a dark red dashed line
line2, = ax.plot(t, y[:, 1], color="#C42121", linestyle="--", linewidth=2, label="Protein (P)")

# Set axis labels
ax.set_xlabel("Time")
ax.set_ylabel("Abundance")

# Set plot title with a larger font size
ax.set_title("Gene Expression Dynamics", fontsize=14, fontweight="bold")

# Set legend with a larger font size
ax.legend(handles=[line1, line2], fontsize=12)

# Add grid lines with a lighter color and dashed style
ax.grid(True, linestyle=":", alpha=0.4, color="#999999")

# Remove top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Customize tick parameters
ax.tick_params(axis="both", which="both", direction="out", length=5, width=1, color="#333333", labelsize=10)

# Set background color for the plot
ax.set_facecolor("#F7F7F7")

# Adjust plot margins
plt.tight_layout()

# Show the plot
plt.show()
