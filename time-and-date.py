import time

current_time = time.strftime("%A, %d %B %Y %H:%M:%S")
print("Right now is:")
print(current_time)
time.sleep(1)

input_value = input("Press enter to close the application: ")
if input_value == "":
    exit()