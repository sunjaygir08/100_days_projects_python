import time

# count = 7
# while count > 0:
#     print(count)
#     time.sleep(1)
#     count -=1
# print("Happy Birthay Sanju!") 

start = int(input("Enter the number to start the countdown from: "))
speed = float(input("Enter the speed of countdown in seconds (e.g., 0.5, 1, 2, 3): "))
if speed < 0.1:
    speed = 0.1
print("#-------Countdown Begins-------#")
while start > 0:
    print(start)
    time.sleep(speed)
    start -= 1
print("Happy Birthday Sanju!")
print("#-------Countdown Ends-------#")