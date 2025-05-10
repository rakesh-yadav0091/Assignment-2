# This function adds temperature to a dictionary if the day is not already present.

def add_daily_temp(temp_dict, day, temp):
    if day not in temp_dict:
        temp_dict[day] = temp
    return temp_dict

temps = {}
day = input("Enter a day: ")
temperature = float(input("Enter temperature: "))
updated = add_daily_temp(temps, day, temperature)
print(updated)