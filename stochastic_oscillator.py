import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import random

# Initial values for G1, G2, G3, and time (t)
G1 = [0]
G2 = [0]
G3 = [0]
t = [0]

tend = 1000

# Parameters for the rates of reactions
k_1 = 2
gamma_1 = 0.1
k_2 = 2
gamma_2 = 0.1
k_3 = 2
gamma_3 = 0.1
n = 9
c = 1

# Simulation loop
while t[-1] < tend:
    current_G1 = G1[-1]
    current_G2 = G2[-1]
    current_G3 = G3[-1]

    # Calculate rates for each reaction
    rates = [(c**n / (c**n + current_G3**n)) * k_1, gamma_1 * current_G1,
             (current_G1**n / (c**n + current_G1**n)) * k_2, gamma_2 * current_G2,
             (current_G2**n / (c**n + current_G2**n)) * k_3, gamma_3 * current_G3]

    rate_sum = sum(rates)

    # Generate a random time step based on the total reaction rate
    tau = np.random.exponential(scale=1/rate_sum)

    # Update time
    t.append(t[-1] + tau)

    rand = random.uniform(0, 1)

    # G1 production event
    if rand * rate_sum <= rates[0]:
        G1.append(G1[-1] + 1)
        G2.append(G2[-1])
        G3.append(G3[-1])

    # G1 decay event
    elif rates[0] < rand * rate_sum <= sum(rates[:2]):
        G1.append(G1[-1] - 1)
        G2.append(G2[-1])
        G3.append(G3[-1])

    # G2 production event
    elif sum(rates[:2]) < rand * rate_sum <= sum(rates[:3]):
        G1.append(G1[-1])
        G2.append(G2[-1] + 1)
        G3.append(G3[-1])

    # G2 decay event
    elif sum(rates[:3]) < rand * rate_sum <= sum(rates[:4]):
        G1.append(G1[-1])
        G2.append(G2[-1] - 1)
        G3.append(G3[-1])

    # G3 production event
    elif sum(rates[:4]) < rand * rate_sum <= sum(rates[:5]):
        G1.append(G1[-1])
        G2.append(G2[-1])
        G3.append(G3[-1] + 1)

    # G3 decay event
    elif sum(rates[:5]) < rand * rate_sum <= sum(rates[:6]):
        G1.append(G1[-1])
        G2.append(G2[-1])
        G3.append(G3[-1] - 1)

# Create a multi-panel plot with shared x-axis
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(10, 8))

# Plot data
ax1.plot(t, G1, color="b", label="G1")
ax2.plot(t, G2, color="r", label="G2")
ax3.plot(t, G3, color="g", label="G3")

# Set axis labels and plot titles
ax3.set_xlabel('Time')
ax1.set_ylabel('Number')
ax2.set_ylabel('Number')
ax3.set_ylabel('Number')
ax1.set_title('Gene Expression over Time')

# Add legends to each subplot
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
ax3.legend(loc='upper right')

# Add grid lines to all subplots
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)

# Adjust layout for better visualization
plt.tight_layout()

# Show the plot
plt.show()
