# Login Attempts
# login_attempts = {
#     "Rahul": 2,
#     "Priya": 6,
#     "Amit": 8,
#     "Neha": 1,
#     "Rohan": 5
# }
# Tasks
# Lock accounts having more than 5 attempts.
# Print remaining users.
# Count locked users.

login_attempts = {
    "Rahul": 2,
    "Priya": 6,
    "Amit": 8,
    "Neha": 1,
    "Rohan": 5,
    "Ayush" : 3,
    "Anu" : 1
}

blocked_user = 0
active_user = 0
new_dict = {}
for users, attempts in login_attempts.items():
    if attempts > 5:
        blocked_user += 1
        login_attempts.pop("Ayush")
        continue
    else:
        # active_user += 1
        new_dict.update(login_attempts)
        print(login_attempts)
        continue

print(blocked_user)
