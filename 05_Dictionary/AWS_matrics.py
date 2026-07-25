metrics = {
    "network" : "80%",
    "CPU": 82,
    "RAM": 65,
    "Disk": 71
}

print(metrics.keys())
print(metrics.items(), "\n")

for key, values in metrics.items():
    print(key, values)


metrics.pop("network") # remove specific item
print(metrics.popitem()) #remove last item  from dict


new_matircs = metrics.copy()
print(new_matircs)

new_matircs.setdefault("Latency" , 40)
print(new_matircs)

print(metrics.clear())

