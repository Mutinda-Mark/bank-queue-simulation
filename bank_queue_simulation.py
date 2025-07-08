# Group 1

import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------
# 🧾 Step 1: Define number of customers
# -------------------------------------------
NUM_CUSTOMERS = 500

# -------------------------------------------
# 🕒 Step 2: Generate Inter-arrival and Service Times
# Uniform distribution as per instructions
# -------------------------------------------
inter_arrival_times = [random.uniform(1, 8) for _ in range(NUM_CUSTOMERS)]
service_times = [random.uniform(1, 6) for _ in range(NUM_CUSTOMERS)]

# -------------------------------------------
# ⏳ Step 3: Simulate Arrival, Service Start, End Times
# -------------------------------------------
arrival_times = []
start_service_times = []
end_service_times = []
waiting_times = []
time_in_system = []

current_time = 0
server_available_time = 0

for i in range(NUM_CUSTOMERS):
    arrival_time = current_time + inter_arrival_times[i]
    arrival_times.append(arrival_time)

    # Determine when the customer can start service
    start_time = max(arrival_time, server_available_time)
    start_service_times.append(start_time)

    # Service completion time
    end_time = start_time + service_times[i]
    end_service_times.append(end_time)

    # Update server availability
    server_available_time = end_time

    # Metrics
    waiting_time = start_time - arrival_time
    total_time = end_time - arrival_time

    waiting_times.append(waiting_time)
    time_in_system.append(total_time)

    current_time = arrival_time  # Move time forward

# -------------------------------------------
# 📊 Step 4: Create a DataFrame for results
# -------------------------------------------
df = pd.DataFrame({
    'Customer': range(1, NUM_CUSTOMERS + 1),
    'InterArrivalTime': inter_arrival_times,
    'ServiceTime': service_times,
    'ArrivalTime': arrival_times,
    'ServiceStartTime': start_service_times,
    'ServiceEndTime': end_service_times,
    'WaitingTime': waiting_times,
    'TimeInSystem': time_in_system
})

# Save to CSV (optional)
df.to_csv("bank_queue_simulation.csv", index=False)

# -------------------------------------------
# 📈 Step 5: Compute Performance Metrics
# -------------------------------------------
print("\n--- Simulation Results ---")
print(f"Average Waiting Time     : {df['WaitingTime'].mean():.2f} minutes")
print(f"Average Service Time     : {df['ServiceTime'].mean():.2f} minutes")
print(f"Average Time in System   : {df['TimeInSystem'].mean():.2f} minutes")
print(f"Maximum Waiting Time     : {df['WaitingTime'].max():.2f} minutes")
print(f"Total Simulation Time    : {df['ServiceEndTime'].max():.2f} minutes")
print(f"Percentage who waited    : {(df['WaitingTime'] > 0).mean() * 100:.2f}%")

# -------------------------------------------
# 📉 Step 6: Visualizations
# -------------------------------------------

# Histogram of waiting times
plt.figure(figsize=(10, 6))
sns.histplot(df['WaitingTime'], bins=30, kde=True, color='skyblue')
plt.title("Distribution of Waiting Times")
plt.xlabel("Waiting Time (minutes)")
plt.ylabel("Number of Customers")
plt.grid(True)
plt.tight_layout()
plt.savefig("waiting_time_distribution.png")
plt.show()

# Line plot of time in system
plt.figure(figsize=(10, 6))
sns.lineplot(x='Customer', y='TimeInSystem', data=df, label='Time in System')
sns.lineplot(x='Customer', y='WaitingTime', data=df, label='Waiting Time')
plt.title("Customer Time in System and Waiting Time")
plt.xlabel("Customer")
plt.ylabel("Time (minutes)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("time_in_system_vs_waiting_time.png")
plt.show()
