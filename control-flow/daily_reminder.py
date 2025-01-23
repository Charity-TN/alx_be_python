
while True:
        task = input("Enter your task: ").strip()
        priority = input("Priority (high,medium,low): ").strip().lower()
        time_bound = input("Is it time-bound? (yes or no): ").strip().lower()

        reminder = ""

        match priority:
            case "high":
                reminder = f"Reminder: {task} is a high-priority task."
            case "medium":
                reminder = f"Reminder: {task} is a medium-priority task.Plan to address it soon."
            case "low":
                reminder = f"Note: {task} is a low-priority task. Consider completing it when you have free time."
            case _:
                    print("Invalid priority. Plaese enter high, medium or low.")

                    continue

        if time_bound == "yes":
            reminder += "This task is time-sensitive and requires immediate attention."
        elif time_bound == "no":
            reminder += "This task is not time-sensitive."
        else:
            print("Invalid input for time-sensitivity. Please enter yes or no.")
    
            continue
        print(f"\n{reminder}")
        break
