# Loop through the list.
# Whenever CPU usage is greater than 80, print:
# Warning! CPU usage is 82%
# At the end print:
# Total warnings
# Highest CPU usage

#Expected output
# Warning! CPU usage is 82%
# Warning! CPU usage is 91%
# Warning! CPU usage is 88%
# Warning! CPU usage is 95%
# Total warnings: 4
# Highest CPU usage: 95%

cpu_usage = [35, 45, 82, 67, 91, 76, 54, 88, 95]

warning_count = 0
for usegae in cpu_usage:
    if usegae > 80:
        print(f"Warning! CPU usage is {usegae}%")
        warning_count += 1

print("Total Warning: ",warning_count)
print("Highest CPU useage: ",max(cpu_usage),"%")