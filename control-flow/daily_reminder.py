task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder:", task, "is high priority task that require immediate attention.")
        else:
            print("Reminder:", task, "is a high priority task with out time bound, consider delegating it.")
    case "medium":
        if time_bound == "yes":
            print("Reminder: Even if", task, "is medium priority, it still have time boundary. Don't ignore it.")
        else:
            print(task, "is medium priority task. Consider doing it later.")
    case "low":
        print("Note:", task, "is a low priority task, consider finishing it with your free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")