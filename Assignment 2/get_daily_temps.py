# This function prompts the user for average temperature for each day of the week.

def get_daily_temps():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    temp_dict = {}
    for day in days:
        temp = float(input(f"Enter temperature for {day}: "))
        temp_dict[day] = temp
    return temp_dict

print(get_daily_temps())