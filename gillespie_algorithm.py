import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import random




# Initialize variables for time and mRNA quantity
X = [0]
t = [0]

tend = 1000

k = 2
gamma = 0.1

# Simulate the stochastic process
while t[-1] < tend:
    current_X = X[-1]

    # Calculate the production and decay rates
    rates = [k, gamma * current_X]
    rate_sum = sum(rates)

    # Sample the waiting time for the next event
    tau = np.random.exponential(scale=1 / rate_sum)

    t.append(t[-1] + tau)

    rand = random.uniform(0, 1)

    # Production event
    if 0 < rand * rate_sum <= rates[0]:
        X.append(X[-1] + 1)
    # Decay event
    elif rates[0] < rand * rate_sum <= rates[0] + rates[1]:
        X.append(X[-1] - 1)

# Create visually stunning plots
plt.figure(figsize=(10, 6))  # Adjusting the figure size

# Plot the mRNA quantity over time
plt.plot(t, X, color="dodgerblue", linewidth=2)
plt.xlabel("Time")
plt.ylabel("mRNA Quantity")
plt.title("Stochastic mRNA Production and Decay")
plt.grid(True, linestyle='--', alpha=0.7)  # Adding gridlines
plt.style.use('seaborn-whitegrid')  # Adding a nice background

# Display the plot
plt.show()
