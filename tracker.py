from datetime import datetime

# 1. Grab the current date and time automatically
current_time = datetime.now().strftime("%Y-%m-%d %I:%M %p")

# 2. Ask what you accomplished
print("What daily task did you complete?")
activity = input("> ")

# 3. Save it straight to a text file
with open("daily_log.txt", "a") as file:
    file.write(f"[{current_time}] {activity}\n")

print(f"Logged successfully: [{current_time}] {activity}")
