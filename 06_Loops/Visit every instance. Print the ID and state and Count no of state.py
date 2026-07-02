

instances = [
    {"id": "i-101", "state": "running"},
    {"id": "i-102", "state": "stopped"},
    {"id": "i-103", "state": "running"},
    {"id": "i-104", "state": "terminated"},
    {"id": "i-105", "state": "running"},
    {"id": "i-106", "state": "stopped"}
]

count_run = 0
count_stop = 0
count_termi = 0

for ec2_instances_data in instances:
    print(ec2_instances_data["id"], ec2_instances_data["state"])

    if ec2_instances_data["state"] == "running":
        count_run += 1
    elif ec2_instances_data["state"] == "stopped":
        count_stop += 1
    else:
        count_termi += 1
print(f"Running instances: {count_run}\nStopped instances: {count_stop}\nTerminated instances: {count_termi}")




# Visit every instance.
# Print the ID and state.
# Count how many instances are:
# Running
# Stopped
# Terminated
# At the end, print the totals.
# Expected Output (format doesn't have to match exactly)
# i-101 -> running
# i-102 -> stopped
# ...

# Running: 3
# Stopped: 2
# Terminated: 1