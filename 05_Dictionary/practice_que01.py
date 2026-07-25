# # Login Attempts
# # login_attempts = {
# #     "Rahul": 2,
# #     "Priya": 6,
# #     "Amit": 8,
# #     "Neha": 1,
# #     "Rohan": 5
# # }
# # Tasks
# # Lock accounts having more than 5 attempts.
# # Print remaining users.
# # Count locked users.




# login_attempts = {
#     "Rahul": 2,
#     "Priya": 6,
#     "Amit": 8,
#     "Neha": 1,
#     "Rohan": 5,
#     "Ayush": 3,
#     "Anu": 1
# }



# blocked_user = 0
# new_dict = {}

# for users, attempts in login_attempts.items():
#     if attempts > 5:
#         blocked_user += 1
#         print(f"{users} is locked — {attempts} attempts")
#     else:
#         new_dict[users] = attempts   # add only this user to new dict

# print(f"\nActive Users: {new_dict}")
# print(f"Locked Users Count: {blocked_user}")


sentence = "python is easy python is powerful python"
result = {}
for word in sentence.split():
    result[word] = result.get(word, 0) + 1
# Slower, more code, no external imports   
print(result)