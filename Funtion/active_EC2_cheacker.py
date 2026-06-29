user = input("Enter state of Instance (Running/Terminated/Stopped): ").lower()

instances = [
    {"id": "101", "state": "running"},
    {"id": "102", "state": "stopped"},
    {"id": "103", "state": "running"},
    {"id": "104", "state": "terminated"},
    {"id": "105", "state": "running"}
]

def active_ec2_checker(instance_list, state):
    count = 0
    for instance in instance_list:
        if instance["state"] == state:
            count += 1

    return count

result = active_ec2_checker(instances, user)

print(f"Number of instances in '{user}' state: {result}")