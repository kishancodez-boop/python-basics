from datetime import datetime

current_time = datetime.now().time()
print("Current time is:", current_time)

if current_time >= datetime.strptime("12:00:00", "%H:%M:%S").time() and current_time <= datetime.strptime("16:00:00", "%H:%M:%S").time():
    print("Good Afternoon")
elif current_time > datetime.strptime("16:00:00", "%H:%M:%S").time() and current_time <= datetime.strptime("20:00:00", "%H:%M:%S").time():
    print("Good Evening")
elif current_time > datetime.strptime("20:00:00", "%H:%M:%S").time() and current_time <= datetime.strptime("23:59:59", "%H:%M:%S").time():
    print("Good Night")
else:
    print("Good Morning")
