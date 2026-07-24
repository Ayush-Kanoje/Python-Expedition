# 20. AWS EC2 CPU Monitoring (Cloud Engineer Scenario)

# CPU usage collected every minute.

# cpu_usage = [30, 45, 82, 91, 75, 68, 95, 40]

# Tasks:

# Count how many times CPU exceeded 80%.
# Print every high usage value.
# Find highest CPU usage.
# Calculate average CPU usage.
# Print "Healthy" if average < 80, otherwise print "Needs Investigation".


cpu_usage = [30, 45, 82, 91, 75, 68, 95, 40]

def cpu_usage_cal(cpu_usage):
    count_useage = 0
    for i in range(len(cpu_usage)): #CPU useage count krega 
        if cpu_usage[i] > 80:
            count_useage += 1
            print(f"CPU Useage Exceed {count_useage}: {cpu_usage[i]} - Needs Investigation")
            continue
        else:
            print(f"Healthy: {cpu_usage[i]}")
    
    print(f"Highest CPU usage {max(cpu_usage)}")

    avg_cpu_useage = sum(cpu_usage)/len(cpu_usage)
    print(avg_cpu_useage)


cpu_usage_cal(cpu_usage)



